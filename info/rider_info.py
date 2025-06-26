from appium import webdriver
from appium.webdriver.appium_service import AppiumService

def get_caps(device):
    if device["platformName"].lower() == "android":
        return {
            "platformName": "Android",

            "udid": device["udid"],
            "platformVersion": device["platformVersion"],
            "automationName": "UiAutomator2",
            "app": "/Users/dajung/Documents/ui_auto/rider_aos_330_1.apk",  # 실기기면 생략 가능
            "appPackage": "io.cubecar.rs.rider",
            "appActivity": "io.cubecar.rs.rider.ui.intro.SplashActivity",
            "systemPort": device["systemPort"]
        }

    elif device["platformName"].lower() == "ios":
        return {
            "platformName": "iOS",

            "udid": device["udid"],
            "platformVersion": device["platformVersion"],
            "automationName": "XCUITest",
            "bundleId": "io.cubecar.rs.riderapp",  # iOS용 번들 ID로 변경
            "xcodeOrgId": "5FG8AK3G25",     # 실기기 테스트시 필요
            "xcodeSigningId": "iPhone Developer",
            "wdaLocalPort": device["systemPort"]  # 병렬 테스트 시 필수
        }

    else:
        raise ValueError("지원하지 않는 platformName입니다. 'Android' 또는 'iOS'여야 합니다.")

# 폴더 경로


def start_appium_server(device):
    service = AppiumService()
    service.start(args=[
        "-p", str(device["appiumPort"])
    ])
    print(f"[INFO] Appium 서버 실행됨 - NAME: {device['name']}, PORT: {device['appiumPort']}")
    return service


# 앱 실행
def rider_appstart(device):
    try:
        print(f"[INFO] {device['udid']} - Appium driver 생성 시도 중...")
        caps = get_caps(device)
        driver = webdriver.Remote(f"http://127.0.0.1:{device['appiumPort']}", caps)
        driver.implicitly_wait(3)
        print(f"[INFO] {device['udid']} - Appium driver 생성 성공")
        return driver
    except Exception as e:
        print(f"[ERROR] {device['udid']} - 앱 실행 중 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        return None
















""" # caps 설정 (기존)
rider_caps = {
    "platformName" : "Android",
    #"deviceName" : "R3CT90F9JJD", # 실제 디바이스 사용 시
    "platformVersion" : "15", # 실행 시 개인 버전 입력
    "app" : "/Users/dajung/Documents/ui_auto/rider_aos_325_2.apk",
    "appPackage" : "io.cubecar.rs.rider",
    "appActivity" : "io.cubecar.rs.rider.ui.intro.SplashActivity",
    "automationName" : "UiAutomator2",
    #"appium:disableIdLocatorAutocompletion": True # 패키지명 미사용
}

# 앱 실행 (기존)
def rider_appstart():
    try:
        print("[INFO] Appium driver 생성 시도 중...")
        driver = webdriver.Remote("http://127.0.0.1:4723", rider_caps)
        driver.implicitly_wait(3)
        print("[INFO] Appium driver 생성 성공")
        return driver
    except Exception as e:
        print(f"[ERROR] 앱 실행 중 오류 발생: {e}")
        return None """