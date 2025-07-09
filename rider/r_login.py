
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from login_info import device_test_data
import unittest, os, base64
from time import sleep

import appium_device_info
from rider.info.rider_info import rider_appstart



# 로그인
class SignIn(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = appium_device_info.driver_instance
        cls.platform = appium_device_info.current_device["platformName"].lower()
        if cls.driver is None:
            raise Exception("RiderStart에서 driver가 설정되지 않았습니다.")

    def test1_login_Button(self):
        try:
            if self.platform == "android":
                button = self.driver.find_element(AppiumBy.ID, "io.cubecar.rs.rider:id/btnLogin")
            elif self.platform == "ios":
                button = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "로그인"`]')  
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            button.click()
            self.driver.implicitly_wait(5)

        except NoSuchElementException:
            self.skipTest("[SKIP] 기 로그인 상태이거나 로그인 버튼 미노출")

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")


    # 이메일 유형 로그인 버튼 클릭
    def test2_email_login_button(self):
        try:
            if self.platform == "android":
                button = self.driver.find_element(AppiumBy.ID, "io.cubecar.rs.rider:id/btnEmail")
            elif self.platform == "ios":
                button = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "이메일로 로그인"`]')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            button.click()
            self.driver.implicitly_wait(5)

        except NoSuchElementException:
            self.skipTest("[SKIP] 기 로그인 상태이거나 로그인 버튼 미노출")

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")
 

        # 이메일 주소 인풋박스 영역 클릭
    def test3_inputbox_tab(self):
        try :
            if self.platform == "android":
                inputbox = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            elif self.platform == "ios":
                inputbox = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            inputbox.click()
            self.driver.implicitly_wait(5)

        except NoSuchElementException:
            self.skipTest("[SKIP] 기 로그인 상태이거나 로그인 버튼 미노출")

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")


    # 아이디_입력 (ID : information.py에 정의된 계정 정보 사용)
    def test4_ID_input(self):
        try:
            
            # 현재 디바이스 UDID 가져오기
            current_udid = appium_device_info.current_device["udid"]
            # 해당 UDID에 맞는 계정 정보 가져오기
            user_info = device_test_data.get(current_udid)

            if not user_info:
                raise Exception(f"{current_udid}에 해당하는 사용자 정보가 없습니다.")

            user_id = user_info["user_id"]

        # 아이디 입력 (ID 필드에 텍스트 입력)
            if self.platform == "android":
                id_field = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            elif self.platform == "ios":
                id_field = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
                
                # 전체 텍스트 선택 → 삭제 → 입력
                id_field.click()
                current_value = id_field.get_attribute("value")
                if current_value:
                    # 전체 선택 + 삭제
                    id_field.clear()
                    # 일부 앱에서는 clear()가 동작 안할 수 있음 → 백스페이스 반복
                    for _ in range(len(current_value)):
                        id_field.send_keys("\b")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            id_field.send_keys(user_id)
            self.driver.implicitly_wait(5)

        except NoSuchElementException:
            self.skipTest("[SKIP] 기 로그인 상태이거나 로그인 버튼 미노출")

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")
        


    # 다음 버튼 클릭
    def test5_next_button(self):
        try :
            if self.platform == "android":
                button = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/next_btn")
            elif self.platform == "ios":
                button = self.driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeButton[`name == "다음"`]')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")

            button.click()
            sleep(3)

        except NoSuchElementException:
            self.skipTest("[SKIP] 기 로그인 상태이거나 로그인 버튼 미노출")

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")
      


    # 비밀번호_입력박스_선택
    def test6_PW_inputbox_tap(self):
        try :
            if self.platform == "android":
                pw_field = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            elif self.platform == "ios":
                pw_field = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeSecureTextField")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")  

            pw_field.click()
            self.driver.implicitly_wait(5)

        except NoSuchElementException:
            self.skipTest("[SKIP] 기 로그인 상태이거나 로그인 버튼 미노출")

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")


    # 비밀번호_입력 (PW : xxxxx)
    def test7_PW_input(self):
        try :
            # 현재 디바이스 UDID 가져오기
            current_udid = appium_device_info.current_device["udid"]
            # 해당 UDID에 맞는 계정 정보 가져오기
            user_info = device_test_data.get(current_udid)

            if not user_info:
                raise Exception(f"{current_udid}에 해당하는 사용자 정보가 없습니다.")

            password = user_info["password"]

        # 비밀번호 입력 (PW 필드에 텍스트 입력)
            if self.platform == "android":
                pw_field = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            elif self.platform == "ios":
                pw_field = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeSecureTextField")
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            pw_field.send_keys(password)
            self.driver.implicitly_wait(5)

        except NoSuchElementException:
            self.skipTest("[SKIP] 기 로그인 상태이거나 로그인 버튼 미노출")

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")


    # 다음 버튼 클릭
    def test8_next_button(self):
        try :
        # 다음 버튼 클릭
            if self.platform == "android": 
                button = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/next_btn")
            elif self.platform == "ios":
                button = self.driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeButton[`name == "다음"`]')
            else:
                raise Exception("지원하지 않는 플랫폼입니다.")
            
            button.click()
            self.driver.implicitly_wait(5)

        except NoSuchElementException:
            self.skipTest("[SKIP] 기 로그인 상태이거나 로그인 버튼 미노출")

        except Exception as e:
            self.fail(f"[FAIL] 예상하지 못한 이슈로 인해 종료: {e}")


    
   