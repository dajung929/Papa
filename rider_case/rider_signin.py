
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rider_information import device_test_data
import unittest
from time import sleep

import appium_driver
from info.rider_info import rider_appstart



# 로그인
class SignIn(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver = appium_driver.driver_instance
        if self.driver is None:
            raise Exception("RiderStart에서 driver가 설정되지 않았습니다.")

    def test1_login_Button(self):
        try:
            if self.platform == "android":
                button = self.driver.find_element(AppiumBy.ID, "io.cubecar.rs.rider:id/btnLogin")
            elif self.platform == "ios":
                button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "btnLogin")  # iOS는 보통 accessibility id 사용
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            button.click()
            self.driver.implicitly_wait(5)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    # 이메일 유형 로그인 버튼 클릭
    def test2_email_login_button(self):
        try:
            if self.platform == "android":
                button = self.driver.find_element(AppiumBy.ID, "io.cubecar.rs.rider:id/btnEmail")
            elif self.platform == "ios":
                button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "btnEmail")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            button.click()
            self.driver.implicitly_wait(5)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

        # 이메일 주소 인풋박스 영역 클릭
    def test3_inputbox_tab(self):
        try :
            if self.platform == "android":
                inputbox = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            elif self.platform == "ios":
                inputbox = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="input_text")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            inputbox.click()
            self.driver.implicitly_wait(5)
        # 오류 추가 (확인용)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    # 아이디_입력 (ID : information.py에 정의된 계정 정보 사용)
    def test4_ID_input(self):
        try:
            
            # 현재 디바이스 UDID 가져오기
            current_udid = appium_driver.current_device["udid"]
            # 해당 UDID에 맞는 계정 정보 가져오기
            user_info = device_test_data.get(current_udid)

            if not user_info:
                raise Exception(f"{current_udid}에 해당하는 사용자 정보가 없습니다.")

            user_id = user_info["user_id"]

        # 아이디 입력 (ID 필드에 텍스트 입력)
            if self.platform == "android":
                id_field = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            elif self.platform == "ios":
                id_field = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="input_text")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            id_field.send_keys(user_id)
            self.driver.implicitly_wait(5)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()


    # 다음 버튼 클릭
    def test5_next_button(self):
        try :
            if self.platform == "android":
                button = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/next_btn")
            elif self.platform == "ios":
                button = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="next_btn")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            button.click()
            sleep(3)
        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()


    # 비밀번호_입력박스_선택
    def test6_PW_inputbox_tap(self):
        try :
            if self.platform == "android":
                pw_field = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            elif self.platform == "ios":
                pw_field = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="input_text")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")  

            pw_field.click()
            self.driver.implicitly_wait(5)
        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    # 비밀번호_입력 (PW : xxxxx)
    def test7_PW_input(self):
        try :
            # 현재 디바이스 UDID 가져오기
            current_udid = appium_driver.current_device["udid"]
            # 해당 UDID에 맞는 계정 정보 가져오기
            user_info = device_test_data.get(current_udid)

            if not user_info:
                raise Exception(f"{current_udid}에 해당하는 사용자 정보가 없습니다.")

            password = user_info["password"]

        # 비밀번호 입력 (PW 필드에 텍스트 입력)
            if self.platform == "android":
                pw_field = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            elif self.platform == "ios":
                pw_field = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="input_text")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            pw_field.send_keys(password)
            self.driver.implicitly_wait(5)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    # 다음 버튼 클릭
    def test8_next_button(self):
        try :
        # 다음 버튼 클릭
            if self.platform == "android": 
                button = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/next_btn")
            elif self.platform == "ios":
                button = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="next_btn")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            button.click()
            self.driver.implicitly_wait(5)
        # 오류 추가 (확인용)
            sleep(3)
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