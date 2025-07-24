from appium import webdriver


crew_caps = {
    "platformName" : "Android",
    #"appium:deviceName" : "실제 디바이스 이름", # 실제 디바이스 사용 시
    "appium:platformVersion" : "14", # 실행 시 개인 버전 입력
    "appium:app" : "/Users/dajung/Documents/ui_auto/crew_137_0.apk",
    "appium:appPackage" : "io.cubecar.rs.driver",
    "appium:appActivity" : "io.cubecar.rs.driver.view.intro.LauncherActivity",
    "appium:ensureWebviewsHavePages" : True,
    "appium:nativeWebScreenshot" : True,
    "appium:newCommandTimeout" : 0,
    "appium:connectHardwareKeyboard" : True, 
    "appium:unicodeKeyboard" : True, 
    "appium:automationName" : "UiAutomator2",
    #"appium:disableIdLocatorAutocompletion": True # 패키지명 미사용
}


# 폴더 경로
main_folder = "/Users/dajung/Documents" # 실행 시 개인 경로 입력

# 슬랙 정보 - 실행 시 개인 정보 입력



# 앱 실행
def crew_start() : 
    try:
        driver = webdriver.Remote("http://127.0.0.1:4723", crew_caps)
        driver.implicitly_wait(3)
        return driver
    except Exception as e:
        print(f"Error starting Appium driver: {e}")
        raise