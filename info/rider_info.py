from appium import webdriver

'''
* 현재 진행중인 내용
로그인
구매입찰
즉시구매
로그인 변경 (아이디 변경)
판매입찰
즉시판매
트레이드 리스트 (검색 등)

* 동작 확인용
1. test case 정상 동작 > 메시지/이미지 수신 없음, 구글에 스크린샷 업로드
 - 구글에 업로드 되는 스크린샷은 상품상세 / 구매/판매 / 리스트 등 확인이 필요한 내용으로 함
2. test case 조회 재시도 / 조회 실패 > 메시지 수신
3. test case 진행 실패 > 메시지/이미지 슬랙 수신, 앱 종료, 구글 드라이브에 결과지 업로드
4. test case 전체 완료 > 구글 드라이브에 결과지 업로드
'''


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