# start.py

import time
import unittest, os
from HtmlTestRunner import HTMLTestRunner
from multiprocessing import Process
import driver_manager
from info.rider_info import start_appium_server
from testcase import rider_start, rider_signin

def run_test_for_device(device):
    # 1. Appium 서버 실행
    os.environ['ANDROID_HOME'] = '/Users/dajung/Library/Android/sdk'
    os.environ['ANDROID_SDK_ROOT'] = '/Users/dajung/Library/Android/sdk'


    driver_manager.current_device = device
    service = start_appium_server(device)

    if not service.is_running:
        print(f"[ERROR] Appium 서버 실행 실패 - {device['udid']}")
        return

    time.sleep(3)  # 안정적 실행 대기

    # 2. 테스트 수트 구성
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(rider_start.execute))
    test_suite.addTests(loader.loadTestsFromTestCase(rider_signin.SignIn))

    # 3. HTML 보고서 출력
    timestamp = time.strftime("%y%m%d_%H.%M")
    file_name = f"UI_Test_{device['name']}"
    report_dir = os.path.join("Reports", timestamp)
    # 폴더가 없으면 생성
    os.makedirs(report_dir, exist_ok=True)

    runner = HTMLTestRunner(
        output=report_dir,
        report_name=file_name,
        report_title=f"{device['name']}",
        combine_reports=False
    )

    print(f"[INFO] {device['name']} - 테스트 시작")
    runner.run(test_suite)

    # 4. Appium 서버 종료
    if service.is_running:
        service.stop()
        print(f"[INFO] Appium 서버 종료 완료 - {device['name']}")


# ▶ 병렬 실행 시작
if __name__ == "__main__":
    processes = []

    for device in driver_manager.device_info:
        p = Process(target=run_test_for_device, args=(device,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("[INFO] 모든 테스트 완료")
