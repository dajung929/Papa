
import datetime
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import unittest

from info.rider_info import rider_start

#서버 자동실행/종료
from appium.webdriver.appium_service import AppiumService
from selenium.common.exceptions import NoSuchElementException


# 앱 실행
class execute(unittest.TestCase):

    # 최초 앱 실행
    @classmethod
    def setUpClass(self):

        # 서버 자동실행 코드 추가 (서버 실행 없이 코드 실행 가능)
        self.appium_service = AppiumService()
        self.appium_service.start(args=['-p', '4723'])

        self.driver = rider_start()
        sleep(5)


    # ** 테스트 케이스 앞 test + 숫자 입력 필수
    # ** test로 test case임을 인식하여 실행
    # ** 01, 02, 03 ... 숫자 순으로 case 실행

    def test01_AOS13_app_push(self):
        max_count = 1
        for _ in range(max_count + 1):

            try:
                self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button").click()
                self.driver.implicitly_wait(5)
                sleep(1)
                #send_slack_message("AOS13 일경우 알림 허용 푸시 - [PASS]")
                break

            except NoSuchElementException:
                if max_count > 0:
                    #send_slack_message("AOS13 알림 팝업 조회 재시도..")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    max_count -= 1
                else:
                    #send_slack_message("AOS13 이상 아님, 알림 팝업 없음")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    print("AOS13 알림 팝업 조회 실패")
                    #self.fail()

            except Exception as e:
                if max_count > 0:
                    #send_slack_message("AOS13 알림 팝업 [허용] 선택 재시도..")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    max_count -= 1
                else:
                    #send_message_screenshot(self.driver, "AOS13 알림 팝업 [허용] 선택 - [Fail], 앱 종료", take_screenshot_and_return_path(self.driver))
                    self.driver.implicitly_wait(5)
                    print(f"실패 사유: {e}")
                    self.driver.quit()
                    self.fail()
                    sleep(1)


    # 혜택_알림(동의)
    # 혜택_알림 팝업 노출 시 실행
    def test03_benefits_alert(self): 
        sleep(3)
        max_count = 1
        for _ in range(max_count + 1):

            try:
                self.driver.find_element(by=AppiumBy.ID, value="com.musinsa.soldout:id/btnPushAgreementOk").click()
                self.driver.implicitly_wait(5)
                sleep(1)
                #send_slack_message("혜택 알림 팝업 [동의] 선택 - [PASS]")
                break

            # ID값을 못찾는 경우
            except NoSuchElementException:
                if max_count > 0:
                    #send_slack_message("혜택 알림 팝업 [동의] 선택 재시도..")
                    self.driverd.implicitly_wait(5)
                    sleep(1)
                    max_count -= 1
                else:
                    #send_slack_message("혜택 알림 팝업 없음")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    print("혜택 알림 팝업 조회 실패")
                    self.fail()

            # 에러가 발생하는 경우
            except Exception as e:
                if max_count > 0:
                    #send_slack_message("혜택 알림 팝업 [동의] 선택 재시도..")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    max_count -= 1
                else:
                    #send_message_screenshot(self.driver, "혜택 알림 팝업 [동의] 선택 - [Fail], 앱 종료", take_screenshot_and_return_path(self.driver))
                    self.driver.implicitly_wait(5)
                    print(f"실패 사유: {e}")
                    self.driver.quit()
                    self.fail()
                    sleep(1)

    # 회원가입_괜찮아요
    # 회원가입 팝업 노출 시 실행
    def test04_signin_alert(self):
        max_count = 1
        for _ in range(max_count + 1):

            try:
                self.driver.find_element(by=AppiumBy.ID, value="com.musinsa.soldout:id/btnHomeLaunchBannerLeft").click()
                self.driver.implicitly_wait(5)
                sleep(1)
                #send_slack_message("회원가입 팝업 [괜찮아요] 선택 - [PASS]")
                break

            except NoSuchElementException:
                if max_count > 0:
                    #send_slack_message("회원가입 팝업 조회 재시도..")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    max_count -= 1
                else:
                    #send_slack_message("회원가입 팝업 없음")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    print("회원가입 팝업 조회 실패")
                    #self.fail()

            except Exception as e:
                if max_count > 0:
                    #send_slack_message("회원가입 팝업 [괜찮아요] 선택 재시도..")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    max_count -= 1
                else:
                    #send_message_screenshot(self.driver, "회원가입 팝업 [괜찮아요] 선택 - [Fail], 앱 종료", take_screenshot_and_return_path(self.driver))
                    self.driver.implicitly_wait(5)
                    print(f"실패 사유: {e}")
                    self.driver.quit()
                    self.fail()
                    sleep(1)
    
    # 메인 배너 닫기
    # 메인 배너 노출 시 실행
    def test05_main_alert(self):
        max_count = 1
        for _ in range(max_count + 1):

            try:
                self.driver.find_element(by=AppiumBy.ID, value="com.musinsa.soldout:id/tvHomePopupBannerRightBtn").click()
                self.driver.implicitly_wait(5)
                sleep(1)
                #send_slack_message("메인 팝업 [닫기] 선택 - [PASS]")
                break

            except NoSuchElementException:
                if max_count > 0:
                    #send_slack_message("메인 팝업 조회 재시도..")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    max_count -= 1
                else:
                    #send_slack_message("메인 팝업 없음")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    self.fail()

            except Exception as e:
                if max_count > 0:
                    #send_slack_message("메인 팝업 [닫기] 선택 재시도..")
                    self.driver.implicitly_wait(5)
                    sleep(1)
                    max_count -= 1
                else:
                    #send_message_screenshot(self.driver, "메인 팝업 [닫기] 선택 - [Fail], 앱 종료", take_screenshot_and_return_path(self.driver))
                    self.driver.implicitly_wait(5)
                    print(f"실패 사유: {e}")
                    self.driver.quit()
                    self.fail()
                    sleep(1)


