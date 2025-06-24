from appium import webdriver
from appium.webdriver.appium_service import AppiumService

def get_caps(device):
    return {
        "platformName": "Android",
        "deviceName": device["udid"],
        "udid": device["udid"],
        "platformVersion": device["platformVersion"],
        "browserName": "Chrome", 
        "automationName": "UiAutomator2",
        "systemPort": device["systemPort"],
        #"chromedriverAutodownload": True, # ChromeDriver 자동 다운로드 설정
        "chromedriverExecutable": device["chomeDriverExecutable"],  # ChromeDriver 경로 설정
        # "appium:disableIdLocatorAutocompletion": True  # 필요시 사용
    }


def start_appium_server(device):
    service = AppiumService()
    service.start(args=[
        "-p", str(device["appiumPort"])
    ])
    print(f"[INFO] Appium 서버 실행됨 - NAME: {device['name']}, PORT: {device['appiumPort']}")
    return service


# 앱 실행
def moweb_start(device):
    try:
        print(f"[INFO] {device['udid']} - Appium driver 생성 시도 중...")
        caps = get_caps(device)
        driver = webdriver.Remote(f"http://127.0.0.1:{device['appiumPort']}", caps)
        driver.get("https://www.google.com")  
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