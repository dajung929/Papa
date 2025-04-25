from appium import webdriver


rider_caps = {
    "platformName" : "Android",
    #"appium:deviceName" : "실제 디바이스 이름", # 실제 디바이스 사용 시
    "appium:platformVersion" : "14", # 실행 시 개인 버전 입력
    "appium:app" : "/Users/m-dajung/Documents/ui_auto/rider_aos_325_2.apk",
    "appium:appPackage" : "com.musinsa.soldout",
    "appium:appActivity" : "com.musinsa.soldout.ui.screen.splash.SplashActivity",
    "appium:ensureWebviewsHavePages" : True,
    "appium:nativeWebScreenshot" : True,
    "appium:newCommandTimeout" : 0,
    "appium:connectHardwareKeyboard" : True, 
    "appium:unicodeKeyboard" : True, 
    "appium:automationName" : "UiAutomator2",
    "appium:disableIdLocatorAutocompletion": True # 패키지명 미사용
}


# 폴더 경로
main_folder = "/Users/dajung/Documents/ui_auto/" # 실행 시 개인 경로 입력

# 슬랙 정보 - 실행 시 개인 정보 입력



# 앱 실행
def rider_start() : 
    driver = webdriver.Remote("http://127.0.0.1:4723", rider_caps)

    driver.implicitly_wait(3)
    return driver