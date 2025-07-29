
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv
load_dotenv()
# 슬랙 설정 

SLACK_TOKEN = os.getenv("SLACK_TOKEN")         
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")
WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

#파일과 함께 메시지를 보내는 함수
def upload_file_v2(file_path, channel_id, message):
    client = WebClient(token=SLACK_TOKEN)
    try:
        response = client.files_upload_v2(
            channel=channel_id,
            file=file_path,
            initial_comment=message
        )
        print("[SUCCESS] 파일 업로드 완료:", response["file"]["name"])
    except SlackApiError as e:
        print("[ERROR] 파일 업로드 실패:", e.response['error'])

# 메시지만 보내는 함수
def send_message(channel_id, message):
    client = WebClient(token=SLACK_TOKEN)
    try:
        response = client.chat_postMessage(
            channel=channel_id,
            text=message
        )
        print("[SUCCESS] 메시지 발송 완료:", response["message"]["text"])
    except SlackApiError as e:
        print("[ERROR] 메시지 발송 실패:", e.response['error'])

