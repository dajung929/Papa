
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from time import sleep
import unittest
import HtmlTestRunner 



# 페이지 구분을 위해 합쳐두지 않음
from testcase import qa_start

#tet


if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    # 주의
    # ** 첫 번째로 실행하는 테스트 케이스 : setUpClass > self.driver = qa_start()
    # ** 이후 이어서 진행 되는 테스트 케이스 : setUpClass > self.driver = test.wd
    #                                                        ㄴ 앞서 진행 되었던 테스트 케이스 클래스의 정보 입력(ex. sapmle 케이스의 test 클래스)



    # ========== 실행할 테스트 케이스 목록 START ========== #
    # (추가한 순서대로 테스트 케이스 실행)

    # 1. 샘플 케이스 실행 (앱 실행 후 광고 배너 팝업 확인 까지)
    # 함수 실행 확인용.
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_start.execute))
    
    # 2. 이어서 진행할 테스트 케이스 (구매자 계정 로그인 xptmxm0)
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_signin.sign_in))

    # 3. 이어서 진행할 테스트 케이스 (마이페이지 - 배송지 추가 // 당장은 필요 없음)
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_mypage.mypage))

    # 4. 구매입찰
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_buy_bid.buy_bid))

    # 5. 즉시구매
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_buy_now.qa_buy))
    
    # id 교체 (판매자 계정으로 변경 milki89)
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_signin_change.sign_in_change))

    # 6. 판매입찰
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_sell_bid.sell_bid))

    # 7. 즉시 판매 케이스 
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_sell_now.sell_now))

    # 8. search 
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_search.search_result))
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_search.search_main))
    #test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(qa_search.search_auto_keyword))


    # ========== 실행할 테스트 케이스 목록 END ========== #



    # 테스트 실행 + 테스트 결과 보고서 파일 생성

    HtmlTestRunner.HTMLTestRunner(
        output="Reports/Logs",
        report_name="Reports",
        report_title="Test Results",
        combine_reports=True
    ).run(test_suite)


    sleep(3)

    # google 드라이브에 reports 파일 업로드
    #reports_upload(reports_folder_id)


    # 테스트 종료 안내 슬랙 메세지 전송
    #send_slack_message("##### 테스트 종료")
    #sleep(1)

    #서버 자동 종료
    @classmethod
    def server_stop(self):
    #서버 자동종료 (코드를 실행시키면 오류 발생, 아래 quit 코드만으로 종료 가능한듯)
        self.appium_service.stop()
        #self.driver.quit()