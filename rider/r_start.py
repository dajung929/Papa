
import datetime
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import unittest
import appium_device_info
from rider.info.rider_info import rider_appstart

from selenium.common.exceptions import NoSuchElementException


# 앱 실행
class execute(unittest.TestCase):

    # 최초 앱 실행
    @classmethod
    def setUpClass(cls):
        device = appium_device_info.current_device
        cls.platform = appium_device_info.current_device["platformName"].lower()

        if device is None:
            raise Exception("device 정보가 설정되어 있지 않습니다.")
        
        cls.driver = rider_appstart(device)
        sleep(3)

        appium_device_info.driver_instance = cls.driver # 다음 테스트 케이스에서 사용할 수 있도록 드라이버 저장

        if cls.driver is None:
            raise Exception("Appium 드라이버 실행 실패. 테스트를 진행할 수 없습니다.")
        sleep(5)
        

        # 접근 권한 페이지 노출될 경우 (ios의 경우 test case 제외)
    def test1_permission1(self):
        if self.platform == "android":
            try:
                # 퍼미션 화면이 노출될 경우 확인 버튼 클릭
                permission_button = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/tv_next")
                permission_button.click()

            except NoSuchElementException:
                self.skipTest("[SKIP] 권한 설정 기 완료로 미표시")

        elif self.platform == "ios":
            self.skipTest("[SKIP] iOS는 권한 팝업 미표시")

        else:
            raise Exception(f"[ERROR] 지원하지 않는 플랫폼입니다: {self.platform}")

        self.driver.implicitly_wait(5)

        # 권한 팝업 (위치정보, 알림, 카메라...)
    def test2_permission2(self): 
        if self.platform == "android":
            try:
                # 위치정보, 카메라 팝업에서 사용중일때 허용 버튼을 2번 클릭
                for _ in range(2):
                    allow_foreground_btn = self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")            
                    allow_foreground_btn.click()
                    sleep(1)

                # 알림 팝업에서 허용 버튼 1번 클릭
                allow_btn = self.driver.find_element(by=AppiumBy.ID,value="com.android.permissioncontroller:id/permission_allow_button")
                allow_btn.click()
                sleep(1)

            except NoSuchElementException:
                self.skipTest("[SKIP] 권한 설정 기 완료로 미표시")

        elif self.platform == "ios":
            self.skipTest("[SKIP] iOS는 권한 팝업 미표시")
            
        else:
            raise Exception(f"[ERROR] 지원하지 않는 플랫폼입니다: {self.platform}")





