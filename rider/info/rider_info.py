from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import traceback

def rider_caps(device):
    if device["platformName"].lower() == "android":
        return {
            "platformName": "Android",
            "udid": device["udid"],
            "platformVersion": device["platformVersion"],
            "automationName": "UiAutomator2",
            #"app": "/Users/dajung/Documents/ui_auto/rider_aos_330_1.apk",  # 실기기면 생략 가능
            "appPackage": "io.cubecar.rs.rider",
            "appActivity": "io.cubecar.rs.rider.ui.intro.SplashActivity",
            "systemPort": device["systemPort"],
            "appium:noReset": True,  # 앱 상태 초기화 방지
        }

    elif device["platformName"].lower() == "ios":
        return {
            "platformName": "iOS",
            "udid": device["udid"],
            "platformVersion": device["platformVersion"],
            "automationName": "XCUITest",
            "bundleId": "io.cubecar.rs.riderapp",  # iOS용 번들 ID
            "xcodeOrgId": "5FG8AK3G25",     
            "xcodeSigningId": "iPhone Developer",
            "wdaLocalPort": device["systemPort"]  # 병렬 테스트 시 필수
        }

    else:
        raise ValueError("지원하지 않는 platformName입니다. 'Android' 또는 'iOS'여야 합니다.")


# Appium 서버 시작
def start_appium_server(device):
    service = AppiumService()
    service.start(args=[
        "-p", str(device["appiumPort"])
    ])
    print(f"[INFO] Appium 서버 실행됨 - NAME: {device['name']}, PORT: {device['appiumPort']}")
    return service


# Appium 드라이버 생성 및 앱 시작
def rider_appstart(device):
    try:
        caps = rider_caps(device)
        driver = webdriver.Remote(f"http://127.0.0.1:{device['appiumPort']}", caps)
        driver.implicitly_wait(3)
        return driver
    except Exception as e:
        traceback.print_exc()
        return None

