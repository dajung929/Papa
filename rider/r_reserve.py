
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_info import device_test_data
import unittest, os, base64
from unittest import SkipTest
from time import sleep
import appium_device_info


# 예약 호출 테스트 케이스
class reserve(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = appium_device_info.driver_instance
        cls.platform = appium_device_info.current_device["platformName"].lower()
        if cls.driver is None:
            raise unittest.SkipTest("driver_instance가 None이라 rider_reserve_call 테스트를 건너뜁니다.")
        
    # 예약 호출 메뉴 진입
    def test1_reserve(self):
        try:
            if self.platform == "android":
                reserve_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.view.View").instance(5)')
  
            elif self.platform == "ios":
                reserve_btn = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
                
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            reserve_btn.click()
            self.driver.implicitly_wait(5)

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")


    # 출발지 설정 1단계
    def test2_pickup_input(self):
        try:
            if self.platform == "android":
                pickup_input = self.driver.find_element(AppiumBy.ID, value='io.cubecar.rs.rider:id/pickUpEditText')
            elif self.platform == "ios":
                pickup_input = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeTextField[`value == "어디서 출발 하시나요?"`]')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            pickup_input.click()
            pickup_input.send_keys("경복궁역")
            self.driver.implicitly_wait(5)

            pickup_item = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='경복궁역[3호선]')
            pickup_item.click()
            sleep(3)

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")

    # 출발지 설정 2단계
    def test3_pickup_set(self):
        try:
            if self.platform == "android":
                pickup_set = self.driver.find_element(AppiumBy.ID, value='io.cubecar.rs.rider:id/request_btn_text')
            elif self.platform == "ios":
                pickup_set = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='출발지 설정')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            pickup_set.click()
            sleep(3)

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")

    # 도착지 설정 1단계
    def test4_pickdrop_input(self):
        try:
            if self.platform == "android":
                pickdrop_input = self.driver.find_element(AppiumBy.ID, value='io.cubecar.rs.rider:id/destEditText')
            elif self.platform == "ios":
                pickdrop_input = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeTextField[`value == "어디로 모실까요?"`]')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            pickdrop_input.click()
            pickdrop_input.send_keys("서울역")
            self.driver.implicitly_wait(5)

            pickdrop_item = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='서울역[1호선]')
            pickdrop_item.click()
            sleep(3)

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")

    # 도착지 설정 2단계
    def test5_pickdrop_set(self):
        try:
            if self.platform == "android":
                pickdrop_set = self.driver.find_element(AppiumBy.ID, value='io.cubecar.rs.rider:id/request_btn_text')
            elif self.platform == "ios":
                pickdrop_set = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='도착지 설정')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            pickdrop_set.click()
            sleep(3)

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")


    # 일자 선택
    def test6_date_set(self):
        try:
            if self.platform == "android":
                date_set = self.driver.find_element(AppiumBy.ID, value='io.cubecar.rs.rider:id/btn_reserve_text')
                date_set.click()

                confirm_btn = self.driver.find_element(AppiumBy.ID, value='io.cubecar.rs.rider:id/confirm_btn')
                confirm_btn.click()

            elif self.platform == "ios":
                date_set = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='예약하기')
                date_set.click()

                confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='icnArrowForward')
                confirm_btn.click()
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            sleep(3)

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")


    # 차종, 결제수단 선택
    def test7_carncash_set(self):
        try:
            # 플랫폼별 locator 정의
            if self.platform == "android":
                selectors = {
                    "cash_applied": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("캐시 적용")'),
                    "cash_unapplied": (AppiumBy.XPATH, '(//android.widget.TextView[@text="미적용"])[2]'),
                    "always_cash": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("항상 캐시 적용")'),
                    "confirm": (AppiumBy.XPATH, '//android.widget.TextView[@text="적용하기"]')
                }

            elif self.platform == "ios":
                selectors = {
                    "cash_applied": (AppiumBy.ACCESSIBILITY_ID, '캐시 적용'),
                    "cash_unapplied": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "미적용"`][2]'),
                    "always_cash": (AppiumBy.ACCESSIBILITY_ID, '항상 캐시 적용'),
                    "confirm": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "적용하기"`]')
                }

            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            # 캐시 적용 상태 확인
            cash_element = self.driver.find_element(*selectors["cash_applied"])
            if cash_element.is_displayed():
                self.skipTest("[SKIP] 캐시 설정 상태")
                return

            # 캐시 미적용 상태일 경우 설정 진행
            self.driver.find_element(*selectors["cash_unapplied"]).click()
            sleep(1)

            self.driver.find_element(*selectors["always_cash"]).click()
            sleep(1)

            self.driver.find_element(*selectors["confirm"]).click()
            sleep(1)
            
        except SkipTest:
            raise

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")
            sleep(3)


        # 예약하기 진행
    def test8_reserve_btn(self):
        try:
            if self.platform == "android":
                btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("예약하기")')
   
            elif self.platform == "ios":
                btn = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText[`name == "예약하기"`]')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            btn.click()
            sleep(3)

            # ▶ 스크린샷 경로 설정 (Reports/{timestamp}/Screenshots/)
            screenshots_dir = os.path.join(appium_device_info.report_dir, "Screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            filename = f"{appium_device_info.current_device['name']}_예약호출 접수완료.png"
            filepath = os.path.join(screenshots_dir, filename)
            self.driver.save_screenshot(filepath)
            print(f"[INFO] 스크린샷 저장 완료: {filepath}")


        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")


        # 확인 버튼 클릭
    def test9_confirm_btn(self):
        try:
            if self.platform == "android":
                btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("확인")')
   
            elif self.platform == "ios":
                btn = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeButton[`name == "확인"`]')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            btn.click()
            sleep(3)

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")



    # 테스트 실패 시 자동 드라이버 종료
    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()
    
