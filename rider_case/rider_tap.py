
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rider_information import device_test_data
import unittest, os, base64
from time import sleep

import drive_device_info
from info.rider_info import rider_appstart



# 하단 탭 바 클릭 테스트 케이스
class Tap(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver = drive_device_info.driver_instance
        self.platform = drive_device_info.current_device["platformName"].lower()
        if self.driver is None:
            raise Exception("RiderStart에서 driver가 설정되지 않았습니다.")

    def test1_main_popup(self):
        try:
            if self.platform == "android":
                button = self.driver.find_element(AppiumBy.ID, "io.cubecar.rs.rider:id/btnLogin")
            elif self.platform == "ios":
                button = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "로그인"`]')  
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            button.click()
            self.driver.implicitly_wait(5)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    # 하단 탭바 중 '전체보기' 클릭
    def test2_total_tap(self):
        try:
            if self.platform == "android":
                button = self.driver.find_element(AppiumBy.ID, "io.cubecar.rs.rider:id/btnEmail")
            elif self.platform == "ios":
                button = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "이메일로 로그인"`]')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            button.click()
            self.driver.implicitly_wait(5)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

        # 하단 탭 바 중 '홈' 클릭
    def test3_Home_tap(self):
        try :
            if self.platform == "android":
                inputbox = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            elif self.platform == "ios":
                inputbox = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            inputbox.click()
            self.driver.implicitly_wait(5)
        # 오류 추가 (확인용)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()


    # 테스트 실패 시 자동 드라이버 종료
    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()
    
    ##### 네트워크 오류 (발생하면 안되는 이슈이나 임시 처리 함)
    #def test08_login_error(self):
    #    self.driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()
    #    sleep(5)