
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
import unittest
import datetime
import HtmlTestRunner 
from selenium import webdriver
from appium.webdriver.appium_service import AppiumService


# 페이지 구분을 위해 합쳐두지 않음
from testcase import rider_start,rider_signin

# Appium 서버 자동 실행
appium_service = AppiumService()
if not appium_service.is_running:
    appium_service.start(args=["-p", "4723"])


# 테스트 수트 구성
test_suite = unittest.TestSuite()

loader = unittest.TestLoader()
test_suite.addTests(loader.loadTestsFromTestCase(rider_start.execute))
test_suite.addTests(loader.loadTestsFromTestCase(rider_signin.SignIn))



# ========== 실행할 테스트 케이스 목록 END ========== #



# 테스트 실행 + 테스트 결과 보고서 파일 생성

HtmlTestRunner.HTMLTestRunner(
    output="Reports",
    report_name="Reports",
    report_title="UI Auto Results",
    combine_reports=True
).run(test_suite)

sleep(3)


# Appium 서버 종료
appium_service.stop()