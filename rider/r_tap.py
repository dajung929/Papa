
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_info import device_test_data
import unittest, os, base64
from time import sleep
import appium_device_info


# 하단 탭 바 클릭 테스트 케이스
class Tap(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = appium_device_info.driver_instance
        cls.platform = appium_device_info.current_device["platformName"].lower()
        if cls.driver is None:
            raise unittest.SkipTest("driver_instance가 None이라 rider_tap 테스트를 건너뜁니다.")

    def test1_main_popup(self):
        try:
            if self.platform == "android":
                main_popup = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.view.View").instance(4)')
                if main_popup.is_displayed():
                    close_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("닫기")') 
                    close_btn.click()
                else:
                    print("메인 팝업 미표기로 PASS")
                    return 

            elif self.platform == "ios":
                main_popup = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeImage')
                if main_popup.is_displayed():
                    close_btn = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText[`name == "닫기"`]') 
                    close_btn.click()
                else:
                    print("메인 팝업 미표기로 PASS")
                    return 
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
                        
            self.driver.implicitly_wait(5)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")


    # 하단 탭바 중 '전체보기' 클릭
    def test2_all_tap(self):
        try:
            if self.platform == "android":
                all_tap = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='전체보기')
            elif self.platform == "ios":
                all_tap = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='전체보기')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            all_tap.click()
            sleep(3)

            # ▶ 스크린샷 경로 설정 (Reports/{timestamp}/Screenshots/)
            screenshots_dir = os.path.join(appium_device_info.report_dir, "Screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            filename = f"{appium_device_info.current_device['name']}_계정.png"
            filepath = os.path.join(screenshots_dir, filename)
            self.driver.save_screenshot(filepath)
            print(f"[INFO] 스크린샷 저장 완료: {filepath}")

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")


        # 하단 탭 바 중 '홈' 클릭
    def test3_Home_tap(self):
        try :
            if self.platform == "android":
                home_tap = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="홈")
            elif self.platform == "ios":
                home_tap = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="홈")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            home_tap.click()
            self.driver.implicitly_wait(5)
        # 오류 추가 (확인용)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
  


