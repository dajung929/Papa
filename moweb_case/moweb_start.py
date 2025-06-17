
import datetime
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import unittest
import appium_driver
from info.moweb_info import moweb_start, get_caps


from selenium.common.exceptions import NoSuchElementException


# 앱 실행
class execute(unittest.TestCase):

    # 최초 앱 실행
    @classmethod
    def setUpClass(self):
        device = appium_driver.current_device
        print(f"[DEBUG] setUpClass device: {device}")

        if device is None:
            raise Exception("device 정보가 설정되어 있지 않습니다.")
        


        self.driver = moweb_start(device)
        sleep(3)
        appium_driver.driver_instance = self.driver
        print(f"[DEBUG] Appium driver 생성 완료: {self.driver}")

        if self.driver is None:
            raise Exception("Appium 드라이버 실행 실패. 테스트를 진행할 수 없습니다.")
        sleep(5)
                # 📌 driver 저장
        


    # ** 테스트 케이스 앞 test + 숫자 입력 필수
    # ** test로 test case임을 인식하여 실행
    # ** 01, 02, 03 ... 숫자 순으로 case 실행

        # 접근 권한 페이지 노출될 경우
    def test1_검색창_인풋클릭 (self):
        try:
            
            button = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="tsf"]/android.view.View[1]/android.widget.EditText')
            button.click()
            button.send_keys("검색")
            self.driver.implicitly_wait(5)


        except NoSuchElementException:
            self.fail("검색창 요소를 찾을 수 없습니다.")


