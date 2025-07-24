
import time
import unittest, os, glob, shutil
from HtmlTestRunner import HTMLTestRunner
from multiprocessing import Process
import appium_device_info
from rider.info.rider_info import start_appium_server
from rider import r_login, r_reserve, r_start, r_tap
from slack_info import upload_file_v2, SLACK_CHANNEL_ID, send_message
from dotenv import load_dotenv
load_dotenv()


def run_test_for_device(device):

    send_message(SLACK_CHANNEL_ID, ":rocket: 자동화 테스트 시작 - " + device['name'])

    # 1. Appium 서버 실행
    os.environ['ANDROID_HOME'] = '/Users/dajung/Library/Android/sdk'
    os.environ['ANDROID_SDK_ROOT'] = '/Users/dajung/Library/Android/sdk'

    appium_device_info.current_device = device
    appium_device_info.driver_instance = None

    try:
        service = start_appium_server(device)
        if not service.is_running:
            print(f"[ERROR] Appium 서버 실행 실패 - {device['udid']}")
            return
    except Exception as e:
        print(f"[ERROR] Appium 서버 실행 중 예외 발생 - {device['udid']}: {str(e)}")
        return
    time.sleep(3)  # 안정적 실행 대기

    # 2. 테스트 수트 구성
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(r_start.execute))
    test_suite.addTests(loader.loadTestsFromTestCase(r_login.SignIn))
    test_suite.addTests(loader.loadTestsFromTestCase(r_tap.Tap))
    #test_suite.addTests(loader.loadTestsFromTestCase(r_reserve.reserve))

    # 3. HTML 보고서 출력
    timestamp = time.strftime("%y%m%d_%H%M%S")
    file_name = f"{device['name']}_{timestamp}"
    report_dir = os.path.join("Reports", timestamp)
    # 폴더가 없으면 생성
    os.makedirs(report_dir, exist_ok=True)

    appium_device_info.report_dir = report_dir
    report_title = f"{device['name']}(OS: {device['platformVersion']})"


    runner = HTMLTestRunner(
        output=report_dir,
        report_name=file_name,
        report_title= report_title,
        combine_reports=True
    )
    runner.run(test_suite)

    # 처리: 방금 리포트 디렉토리에서 가장 최신 파일 찾기
    files = glob.glob(os.path.join(report_dir, "*.html"))
    latest_file = max(files, key=os.path.getctime)

    # 원하는 이름으로 리네임
    desired_path = os.path.join(report_dir, f"{file_name}.html")
    shutil.move(latest_file, desired_path)

    # 4. Appium 서버 종료
    if service.is_running:
        service.stop()
        # 안전한 로깅을 위해 사용자 입력값 사용 전 새니타이즈
        safe_device_name = ''.join(c for c in device['name'] if c.isalnum() or c in [' ', '-', '_']).strip()
        print(f"[INFO] Appium 서버 종료 - {safe_device_name}")

    # 5. Slack 알림

    safe_filename = os.path.basename(f"{file_name}.html")
    report_file = os.path.join(report_dir, safe_filename)
    message = f":white_check_mark: 자동화 테스트 완료 - {safe_device_name}"

    if os.path.exists(report_file):
        upload_file_v2(desired_path, SLACK_CHANNEL_ID, message)
    else:
        print(f"[INFO] 리포트 파일이 존재하지 않아 Slack 전송 생략: {report_file}")


# ▶ 병렬 실행 시작
if __name__ == "__main__":
    processes = []

    for devices in appium_device_info.device_info:
        p = Process(target=run_test_for_device, args=(devices,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("[INFO] 모든 테스트 완료")
