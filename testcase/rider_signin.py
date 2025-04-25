
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

import unittest
from time import sleep

from info.rider_info import rider_start
from testcase.rider_start import execute


# 로그인
class sign_in(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        
        self.driver = execute.driver
        self.driver.implicitly_wait(5)

    def test1_login_Button(self):
        try :
            button = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/btnLogin")
            button.click()
            self.driver.implicitly_wait(5)
        # 오류 추가 (확인용)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    # 이메일 유형 로그인 버튼 클릭
    def test2_email_login_button(self):
        try :
            button = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/btnEmail")
            button.click()
            self.driver.implicitly_wait(5)
        # 오류 추가 (확인용)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

        # 이메일 주소 인풋박스 영역 클릭
    def test3_inputbox_tab(self):
        try :
            inputbox = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            inputbox.click()
            self.driver.implicitly_wait(5)
        # 오류 추가 (확인용)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    # 아이디_입력 (ID : djtest3@papa.com)
    def test4_ID_input(self):
        try :
            # 아이디 입력 (ID 필드에 텍스트 입력)
            input_field = self.driver.find_element_by_id("io.cubecar.rs.rider:id/input_text")
            input_field.send_keys("djtest3@papa.com") 
            self.driver.implicitly_wait(5)
        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    # 다음 버튼 클릭
    def test5_next_button(self):
        try :
            button = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/next_btn")
            button.click()
            self.driver.implicitly_wait(5)
        # 오류 추가 (확인용)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()


    # 비밀번호_입력박스_선택
    def test6_PW_inputbox_tap(self):
        try :
            inputbox = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/input_text")
            inputbox.click()
            self.driver.implicitly_wait(5)
        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    # 비밀번호_입력 (PW : xxxxx)
    def test07_PW_input(self):
        try :
            input_field = self.driver.find_element_by_id("io.cubecar.rs.rider:id/input_text")
            input_field.send_keys("test12345!") 
            self.driver.implicitly_wait(5)
        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    # 다음 버튼 클릭
    def test8_next_button(self):
        try :
            button = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/next_btn")
            button.click()
            self.driver.implicitly_wait(5)
        # 오류 추가 (확인용)

        except Exception as e:
            print(f"예상하지 못한 이슈로 인해 종료: {e}")
            self.driver.quit()

    
    ##### 네트워크 오류 (발생하면 안되는 이슈이나 임시 처리 함)
    #def test08_login_error(self):
    #    self.driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()
    #    sleep(5)