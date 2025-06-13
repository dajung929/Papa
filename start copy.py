
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
import unittest
import time
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from appium.webdriver.appium_service import AppiumService
from info.rider_info import device_info, start_appium_server

# 페이지 구분을 위해 합쳐두지 않음
from testcase import rider_start,rider_signin

# Appium 서버 자동 실행
appium_services = []
for device in device_info:
    service = start_appium_server(device)
    appium_services.append((service,device))


# 테스트 수트 구성
test_suite = unittest.TestSuite()

loader = unittest.TestLoader()
test_suite.addTests(loader.loadTestsFromTestCase(rider_start.execute))
test_suite.addTests(loader.loadTestsFromTestCase(rider_signin.SignIn))



# ========== 실행할 테스트 케이스 목록 END ========== #



# 테스트 실행 + 테스트 결과 보고서 파일 생성

def run_test_for_device(device):
    test_suite = unittest.TestLoader().discover('tests')  # 테스트 경로에 맞게

    timestamp = time.strftime("%Y%m%d_%H%M")
    file_name = f"UI Test_{device['udid']}_{timestamp}"

    runner = HTMLTestRunner(
        output="Reports",
        report_name=file_name,
        report_title=f"UI 테스트 결과 - {device['name']}",
        combine_reports=True
    )
    runner.run(test_suite)


for service, device in appium_services:
    if service.is_running:
        service.stop()
        print("[INFO] Appium 서버 종료 완료")