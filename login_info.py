import appium_device_info

# device_info 리스트 순서에 맞춘 테스트 계정 정보 리스트
test_accounts = [
    {
        "user_id": "djtest3@papa.com",
        "password": "test12345!"
    },
    {
        "user_id": "djtest4@papa.com",
        "password": "test12345!"
    },
       {
        "user_id": "djtest5@papa.com",
        "password": "test12345!"
    }
]

# 순서대로 udid -> 계정 정보 매핑 딕셔너리 생성
device_test_data = {}

for i, appium_devices in enumerate(appium_device_info.device_info):
    if i < len(test_accounts):
        device_test_data[appium_devices["udid"]] = test_accounts[i]
    else:
        # test_accounts보다 device_info가 더 많을 때 기본값 지정
        device_test_data[appium_devices["udid"]] = {
            "user_id": "djtest6@papa.com",
            "password": "test12345!"
        }
