
import datetime
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import unittest

from info.rider_info import rider_appstart

#서버 자동실행/종료
from appium.webdriver.appium_service import AppiumService
from selenium.common.exceptions import NoSuchElementException


# 앱 실행
class execute(unittest.TestCase):

    # 최초 앱 실행
    @classmethod
    def setUpClass(self):

        # 서버 자동실행 코드 추가 (서버 실행 없이 코드 실행 가능)
        #self.appium_service = AppiumService()
        #self.appium_service.start(args=['-p', '4723'])

        self.driver = rider_appstart()
        sleep(5)


    # ** 테스트 케이스 앞 test + 숫자 입력 필수
    # ** test로 test case임을 인식하여 실행
    # ** 01, 02, 03 ... 숫자 순으로 case 실행

        # 접근 권한 페이지 노출될 경우
        def test1_permission(self):
            try:
                # 퍼미션 화면이 노출될 경우 확인 버튼 클릭
                permission_button = self.driver.find_element(by=AppiumBy.ID, value="io.cubecar.rs.rider:id/tv_next")
                permission_button.click()
                self.driver.implicitly_wait(5)
                sleep(1)


            except NoSuchElementException:
                print("요소를 찾을 수 없어 test2로 넘어갑니다.")
                self.test3()


        # 권한 팝업 (위치정보, 알림, 카메라...)
        def test2_permission_popup(self): 
            try:
                # 위치정보, 카메라 팝업에서 사용중일때 허용 버튼을 2번 클릭
                for _ in range(2):
                    allow_foreground_btn = self.driver.find_element(
                        by=AppiumBy.ID,
                        value="com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                    allow_foreground_btn.click()
                    sleep(1)

                # 알림 팝업에서 허용 버튼 1번 클릭
                allow_btn = self.driver.find_element(
                    by=AppiumBy.ID,
                    value="com.android.permissioncontroller:id/permission_allow_button"
                )
                allow_btn.click()
                sleep(1)

            except NoSuchElementException as e:
                print("권한 팝업 버튼을 찾을 수 없습니다:", e)





