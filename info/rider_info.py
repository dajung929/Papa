from appium import webdriver


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


# 폴더 경로
main_folder = "/Users/dajung/Documents" # 실행 시 개인 경로 입력

# 슬랙 정보 - 실행 시 개인 정보 입력



# 앱 실행
def rider_appstart():
    try:
        print("[INFO] Appium driver 생성 시도 중...")
        driver = webdriver.Remote("http://127.0.0.1:4723", rider_caps)
        driver.implicitly_wait(3)
        print("[INFO] Appium driver 생성 성공")
        return driver
    except Exception as e:
        print(f"[ERROR] 앱 실행 중 오류 발생: {e}")
        return None