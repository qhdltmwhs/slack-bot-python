import os  # 운영체제와 상호작용 (파일 경로, 디렉토리 생성 등)
import csv  # CSV 파일 읽기/쓰기 모듈
from slack_bolt import App  # Slack Bolt 프레임워크의 App 클래스 임포트 (Slack 앱 생성 및 이벤트 핸들링)
from slack_bolt.adapter.socket_mode import SocketModeHandler  # 소켓 모드 핸들러 (개발 중 로컬에서 봇 실행을 위함)
from dotenv import load_dotenv  # .env 파일에서 환경 변수를 로드하기 위한 모듈
from datetime import datetime  # 날짜 및 시간 정보 처리를 위함
from slack_sdk import WebClient  # Slack Web API 호출을 위한 클라이언트 (파일 업로드, DM 열기 등)

# .env 파일 로드: SLACK_BOT_TOKEN 및 SLACK_APP_TOKEN과 같은 환경 변수를 현재 환경으로 로드합니다.
# 이 변수들은 봇을 실행하고 Slack API와 통신하는 데 사용됩니다.
load_dotenv()

# Slack 앱 초기화:
# 환경 변수에서 SLACK_BOT_TOKEN을 가져와 봇 인스턴스를 생성합니다.
# 이 토큰은 봇이 Slack 워크스페이스 내에서 작업을 수행할 수 있도록 인증합니다.
app = App(token=os.environ["SLACK_BOT_TOKEN"])


# --- JSON 예시 (실제 코드 실행과 무관하며, API 응답 구조 이해를 돕기 위함) ---
# @app.command("/제출") 명령어가 수신될 때 Slack에서 봇으로 전송되는 JSON 'body' 파라미터의 예시입니다.
# 이 데이터는 명령어 실행 시의 사용자, 채널, 트리거 ID 등의 정보를 포함합니다.
# 'trigger_id'는 모달(Modal) 창을 여는 데 필수적으로 사용됩니다.
"""
{
    "token": "lTJNImiDDZe6kNQuqABlYDAe",
    "team_id": "T08TDQNJDUJ",
    "team_domain": "qhdltmwhs",
    "channel_id": "C08TJM1RG2E",
    "channel_name": "test",
    "user_id": "U08TDQNJE10",
    "user_name": "qhdltmwhs",
    "command": "/제출",
    "text": "",
    "api_app_id": "A092UFX0E4A",
    "is_enterprise_install": "false",
    "response_url": "https://hooks.slack.com/commands/T08TDQNJDUJ/9085180773399/LVXK3rKtTO9FF3VBhb0yR0wv",
    "trigger_id": "9085180778055.8931838625970.032aefbbce14bbf4dcb21f7b0ae4f540",
}
"""

# @app.view("submit_view") 콜백 함수가 수신될 때 Slack에서 봇으로 전송되는 JSON 'body' 파라미터의 예시입니다.
# 이는 사용자가 모달 폼을 제출했을 때의 데이터 구조를 보여주며,
# 입력된 값들이 'view.state.values' 내에 블록 ID와 액션 ID를 키로 저장되어 있음을 나타냅니다.
"""
{
    "type": "view_submission",
    "team": {"id": "T08TDQNJDUJ", "domain": "qhdltmwhs"},
    "user": {
        "id": "U08TDQNJE10",
        "username": "qhdltmwhs",
        "name": "qhdltmwhs",
        "team_id": "T08TDQNJDUJ",
    },
    "api_app_id": "A092UFX0E4A",
    "token": "lTJNImiDDZe6kNQuqABlYDAe",
    "trigger_id": "9085508157239.8931838625970.469d220d3cafd563e5928b0c1d086517",
    "view": {
        "id": "V092S1M0RSA",
        "team_id": "T08TDQNJDUJ",
        "type": "modal",
        "blocks": [
            {
                "type": "input",
                "block_id": "title_block_id",
                "label": {"type": "plain_text", "text": "제목", "emoji": True},
                "optional": False,
                "dispatch_action": False,
                "element": {
                    "type": "plain_text_input",
                    "action_id": "input_action_id",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "뉴진스",
                        "emoji": True,
                    },
                    "multiline": False,
                    "dispatch_action_config": {
                        "trigger_actions_on": ["on_enter_pressed"]
                    },
                },
            },
            {
                "type": "input",
                "block_id": "contents_block_id",
                "label": {"type": "plain_text", "text": "컨텐츠", "emoji": True},
                "optional": False,
                "dispatch_action": False,
                "element": {
                    "type": "plain_text_input",
                    "action_id": "input_action_id",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "강해린",
                        "emoji": True,
                    },
                    "multiline": True,
                    "dispatch_action_config": {
                        "trigger_actions_on": ["on_enter_pressed"]
                    },
                },
            },
            {
                "type": "input",
                "block_id": "comment_block_id",
                "label": {"type": "plain_text", "text": "의견", "emoji": True},
                "optional": True,
                "dispatch_action": False,
                "element": {
                    "type": "plain_text_input",
                    "action_id": "input_action_id",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "최애 걸그룹 멤버",
                        "emoji": True,
                    },
                    "multiline": True,
                    "dispatch_action_config": {
                        "trigger_actions_on": ["on_enter_pressed"]
                    },
                },
            },
        ],
        "private_metadata": "C08TJM1RG2E",
        "callback_id": "submit_view",
        "state": {
            "values": {
                "title_block_id": {
                    "input_action_id": {"type": "plain_text_input", "value": "뉴진스"}
                },
                "contents_block_id": {
                    "input_action_id": {"type": "plain_text_input", "value": "강해린"}
                },
                "comment_block_id": {
                    "input_action_id": {
                        "type": "plain_text_input",
                        "value": "걸그룹 멤버",
                    }
                },
            }
        },
        "hash": "1750823284.P0IHmfHd",
        "title": {"type": "plain_text", "text": "모달 폼 테스트", "emoji": True},
        "clear_on_close": False,
        "notify_on_close": False,
        "close": {"type": "plain_text", "text": "취소", "emoji": True},
        "submit": {"type": "plain_text", "text": "제출", "emoji": True},
        "previous_view_id": None,
        "root_view_id": "V092S1M0RSA",
        "app_id": "A092UFX0E4A",
        "external_id": "",
        "app_installed_team_id": "T08TDQNJDUJ",
        "bot_id": "B092MNXLW1H",
    },
    "response_urls": [],
    "is_enterprise_install": False,
    "enterprise": None,
}
"""

# @app.view("submit_view")에서 client.users_info(user=body["user"]["id"]) 호출 시 반환되는 JSON 예시입니다.
# 이 데이터는 특정 사용자 ID에 대한 상세 프로필 정보를 포함합니다.
"""
{
    "ok": True,
    "user": {
        "id": "U08TDQNJE10",
        "name": "qhdltmwhs",
        "is_bot": False,
        "updated": 1748325557,
        "is_app_user": False,
        "team_id": "T08TDQNJDUJ",
        "deleted": False,
        "color": "902d59",
        "is_email_confirmed": True,
        "real_name": "모네",
        "tz": "Asia/Seoul",
        "tz_label": "Korea Standard Time",
        "tz_offset": 32400,
        "is_admin": True,
        "is_owner": True,
        "is_primary_owner": True,
        "is_restricted": False,
        "is_ultra_restricted": False,
        "who_can_share_contact_card": "EVERYONE",
        "profile": {
            "real_name": "모네",
            "display_name": "모네",
            "avatar_hash": "13d383bfe86d",
            "real_name_normalized": "모네",
            "display_name_normalized": "모네",
            "image_24": "https://avatars.slack-edge.com/2025-05-21/8927751326613_13d383bfe86d3a6eeb29_24.jpg",
            "image_32": "https://avatars.slack-edge.com/2025-05-21/8927751326613_13d383bfe86d3a6eeb29_32.jpg",
            "image_48": "https://avatars.slack-edge.com/2025-05-21/8927751326613_13d383bfe86d3a6eeb29_48.jpg",
            "image_72": "https://avatars.slack-edge.com/2025-05-21/8927751326613_13d383bfe86d3a6eeb29_72.jpg",
            "image_192": "https://avatars.slack-edge.com/2025-05-21/8927751326613_13d383bfe86d3a6eeb29_192.jpg",
            "image_512": "https://avatars.slack-edge.com/2025-05-21/8927751326613_13d383bfe86d3a6eeb29_512.jpg",
            "image_1024": "https://avatars.slack-edge.com/2025-05-21/8927751326613_13d383bfe86d3a6eeb29_1024.jpg",
            "image_original": "https://avatars.slack-edge.com/2025-05-21/8927751326613_13d383bfe86d3a6eeb29_original.jpg",
            "is_custom_image": True,
            "first_name": "모네",
            "last_name": "",
            "team": "T08TDQNJDUJ",
            "title": "",
            "phone": "",
            "skype": "",
            "status_text": "",
            "status_text_canonical": "",
            "status_emoji": "",
            "status_emoji_display_info": [],
            "status_expiration": 0,
        },
    },
}
"""

# @app.action("fetch_all_submission") 콜백 함수가 수신될 때 Slack에서 봇으로 전송되는 JSON 'body' 파라미터의 예시입니다.
# 이는 "전체 제출내역 조회" 버튼과 같은 Block Kit 액션이 발생했을 때의 데이터 구조를 보여줍니다.
"""
{
    "type": "block_actions",
    "user": {
        "id": "U08TDQNJE10",
        "username": "qhdltmwhs",
        "name": "qhdltmwhs",
        "team_id": "T08TDQNJDUJ",
    },
    "api_app_id": "A092UFX0E4A",
    "token": "lTJNImiDDZe6kNQuqABlYDAe",
    "container": {
        "type": "message",
        "message_ts": "1750855711.001000",
        "channel_id": "C08TJM1RG2E",
        "is_ephemeral": True,
    },
    "trigger_id": "9095272100611.8931838625970.9fc649307ba6dd73fdd98443b1e7c8c8",
    "team": {"id": "T08TDQNJDUJ", "domain": "qhdltmwhs"},
    "enterprise": None,
    "is_enterprise_install": False,
    "channel": {"id": "C08TJM1RG2E", "name": "test"},
    "state": {"values": {}},
    "response_url": "https://hooks.slack.com/actions/T08TDQNJDUJ/9095272082035/6TOsbTHTPGnq6ZqYzJDhtVzt",
    "actions": [
        {
            "action_id": "fetch_all_submission",
            "block_id": "4N7BG",
            "text": {"type": "plain_text", "text": "전체 제출내역 조회", "emoji": True},
            "value": "admin_value_1",
            "type": "button",
            "action_ts": "1750855713.631129",
        }
    ],
}
"""

# Slack 슬래시 명령어 `/제출`에 대한 핸들러 함수입니다.
# 사용자가 `/제출` 명령어를 입력하면 모달 폼을 열어 데이터를 입력받습니다.
@app.command("/제출")
def handle_submit_command(ack, body, client):
    # Slack 요청을 즉시 승인합니다. ack() 없이는 봇이 응답하지 않아 사용자에게 오류가 발생한 것처럼 보일 수 있습니다.
    ack()
    
    # Slack WebClient를 사용하여 'views_open' API를 호출하여 모달 폼을 엽니다.
    client.views_open(
        # 'trigger_id'는 Slack에서 받은 요청에 대한 고유 ID로, 모달을 여는 데 3초 이내에 사용해야 합니다.
        trigger_id=body["trigger_id"],
        # 모달의 전체 페이로드(JSON 구조)를 정의합니다.
        view={
            "type": "modal",  # 뷰의 타입은 모달입니다.
            "callback_id": "submit_view",  # 이 모달에서 제출 이벤트 발생 시 호출될 콜백 ID입니다.
            # 'private_metadata': 모달 제출 시 콜백 함수로 전달될 추가 데이터입니다.
            # 여기서는 명령어가 실행된 채널 ID를 저장하여, 모달 제출 후 해당 채널로 메시지를 보낼 때 사용합니다.
            "private_metadata": body["channel_id"],
            "title": {"type": "plain_text", "text": "모달 폼 테스트"},  # 모달 제목
            "close": {"type": "plain_text", "text": "취소"},  # 닫기 버튼 텍스트
            "submit": {"type": "plain_text", "text": "제출"},  # 제출 버튼 텍스트
            "blocks": [
                # 제목 입력 필드 정의
                {
                    "type": "input",  # 입력 블록 타입
                    "block_id": "title_block_id",  # 이 입력 블록의 고유 ID
                    "label": {
                        "type": "plain_text",
                        "text": "제목",  # 입력 필드 레이블
                    },
                    "element": {
                        "type": "plain_text_input",  # 단일 라인 텍스트 입력 요소
                        "action_id": "input_action_id",  # 입력 요소의 고유 액션 ID
                        "multiline": False,  # 여러 줄 입력 비활성화
                        "placeholder": {"type": "plain_text", "text": "뉴진스"},  # 플레이스홀더 텍스트
                    },
                },
                # 컨텐츠 입력 필드 정의
                {
                    "type": "input",
                    "block_id": "contents_block_id",
                    "label": {
                        "type": "plain_text",
                        "text": "컨텐츠",
                    },
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "input_action_id",
                        "multiline": True,  # 여러 줄 입력 활성화
                        "placeholder": {"type": "plain_text", "text": "강해린"},
                    },
                },
                # 의견 입력 필드 정의 (선택 사항)
                {
                    "type": "input",
                    "block_id": "comment_block_id",
                    "optional": True,  # 이 필드는 필수가 아님을 나타냅니다.
                    "label": {
                        "type": "plain_text",
                        "text": "의견",
                    },
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "input_action_id",
                        "multiline": True,
                        "placeholder": {
                            "type": "plain_text",
                            "text": "최애 걸그룹 멤버",
                        },
                    },
                },
            ],
        },
    )


# 모달 폼의 제출(submission) 이벤트에 대한 핸들러 함수입니다.
# 'callback_id'가 "submit_view"인 모달이 제출되면 이 함수가 호출됩니다.
@app.view("submit_view")
def handle_view_submission_events(ack, body, client):
    # 'private_metadata'에서 채널 ID를 가져옵니다. 이 값은 모달을 열 때 저장되었습니다.
    channel_id = body["view"]["private_metadata"]

    # --- 제출 채널 유효성 검사 ---
    # 모달이 특정 채널 (여기서는 "C08TJM1RG2E" - 'test' 채널)에서만 유효한지 확인합니다.
    if channel_id != "C08TJM1RG2E":
        # 유효성 검사 실패 시, 'response_action="errors"'를 사용하여 Slack에 오류 메시지를 반환합니다.
        # 'errors' 딕셔너리의 키는 모달 폼 내의 'block_id'와 일치해야 합니다.
        ack(
            response_action="errors",
            errors={"contents_block_id": "#test 채널에서만 제출할 수 있습니다."},
        )
        # 오류가 발생했으므로 더 이상의 처리를 중단하고 함수를 종료합니다.
        return None

    # --- 컨텐츠 글자 수 유효성 검사 ---
    # 모달 폼에서 'contents_block_id'의 'input_action_id'에 해당하는 입력 값을 가져옵니다.
    contents = body["view"]["state"]["values"]["contents_block_id"]["input_action_id"][
        "value"
    ]
    # 컨텐츠 길이가 3글자 미만인지 확인합니다.
    if len(contents) < 3:
        # 유효성 검사 실패 시, 동일하게 오류 메시지를 반환합니다.
        ack(
            response_action="errors",
            errors={"contents_block_id": "컨텐츠는 세 글자 이상 입력해주세요."},
        )
        # 오류가 발생했으므로 함수를 종료합니다.
        return None
        
    # 모든 유효성 검사를 통과했으므로 Slack 요청을 최종적으로 승인합니다.
    # ack() 호출은 Slack이 봇이 요청을 성공적으로 처리했음을 알리는 역할을 합니다.
    ack()

    # --- 저장할 데이터 추출 ---
    # Slack API 'body'에서 사용자 ID를 추출합니다.
    user_id = body["user"]["id"]
    # 'client.users_info' API를 호출하여 사용자 ID를 기반으로 상세 사용자 정보(실제 이름 등)를 가져옵니다.
    user_info = client.users_info(user=user_id)
    # 사용자 정보에서 실제 이름을 추출합니다.
    user_name = user_info["user"]["real_name"]
    
    # 모달 폼에서 입력된 '제목' 값을 추출합니다.
    title = body["view"]["state"]["values"]["title_block_id"]["input_action_id"][
        "value"
    ]
    # 모달 폼에서 입력된 '컨텐츠' 값을 추출합니다.
    contents = body["view"]["state"]["values"]["contents_block_id"]["input_action_id"][
        "value"
    ]
    # 모달 폼에서 입력된 '의견' 값을 추출합니다. (선택 필드이므로 값이 없을 수도 있습니다)
    comment = body["view"]["state"]["values"]["comment_block_id"]["input_action_id"][
        "value"
    ]
    # 현재 시간을 'YYYY-MM-DD HH:MM:SS' 형식의 문자열로 포맷팅합니다.
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # --- 데이터 디렉토리 생성 ---
    # 'data' 디렉토리가 존재하지 않으면 생성합니다.
    if not os.path.exists("data"):
        os.makedirs("data")

    # --- 제출 정보를 CSV 파일에 저장 ---
    # 'data/db.csv' 파일을 추가 모드('a')로 엽니다. 'newline=""'은 CSV 파일의 줄 바꿈 문제를 방지합니다.
    with open("data/db.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # 파일 크기가 0바이트(즉, 비어있음)보다 크지 않다면 (파일이 비어있다면), 헤더 행을 먼저 추가합니다.
        if not os.path.getsize("data/db.csv") > 0:
            writer.writerow(
                ["user_id", "user_name", "title", "contents", "comment", "created_at"]
            )
        
        # 추출된 데이터를 CSV 파일에 한 행으로 작성합니다.
        writer.writerow([user_id, user_name, title, contents, comment, created_at])

    # --- 슬랙 채널에 완료 안내 메시지 보내기 ---
    # 사용자에게 보낼 메시지 텍스트를 구성합니다.
    # <@{user_id}>는 Slack에서 해당 사용자를 멘션하는 효과를 줍니다.
    text = f">>> *<@{user_id}>님이 `{title}`의 *\n\n '{contents}'에 대해 \n"
    # '의견'이 있다면 메시지에 추가합니다.
    if comment:
        text += f"\n {comment} 의견 공유 \n"
    
    # 'client.chat_postMessage' API를 호출하여 Slack 채널에 메시지를 게시합니다.
    # 'channel'은 모달을 열 때 저장했던 채널 ID를 사용합니다.
    client.chat_postMessage(channel=channel_id, text=text)


# Slack 슬래시 명령어 `/조회`에 대한 핸들러 함수입니다.
# 사용자가 자신의 제출 내역을 조회하고자 할 때 사용됩니다.
@app.command("/조회")
def handle_submission_history_command(ack, body, client: WebClient):
    # Slack 요청을 즉시 승인합니다.
    ack()

    # --- 멤버의 DM 채널 ID 가져오기 ---
    # 명령어를 실행한 사용자의 ID를 추출합니다.
    user_id = body["user_id"]
    # 'client.conversations_open' API를 호출하여 특정 사용자(들)와의 DM 채널을 엽니다.
    # 만약 이미 열려 있다면 해당 채널 정보를 반환하고, 없다면 새로 생성합니다.
    response = client.conversations_open(users=user_id)
    # 응답에서 DM 채널의 ID를 추출합니다.
    dm_channel_id = response["channel"]["id"]

    # --- 제출내역 파일 존재 여부 확인 ---
    # 'data/db.csv' 파일이 존재하지 않는 경우 (아무도 제출한 적이 없는 경우)
    if not os.path.exists("data/db.csv"):
        # 사용자 DM 채널에 제출내역이 없다는 메시지를 전송하고 함수를 종료합니다.
        client.chat_postMessage(
            channel=dm_channel_id, text="전체 멤버의 제출내역이 없습니다."
        )
        return None

    # --- 멤버의 제출내역 필터링 ---
    submission_list = []  # 사용자 제출 내역을 저장할 리스트 초기화
    # 'data/db.csv' 파일을 읽기 모드로 엽니다.
    with open("data/db.csv") as csvfile:
        # 'csv.DictReader'를 사용하여 CSV 파일의 첫 행을 헤더(키)로 사용하여 각 행을 딕셔너리 형태로 읽어옵니다.
        reader = csv.DictReader(csvfile)
        # CSV 파일의 헤더(필드명)를 저장합니다. 임시 파일 생성 시 필요합니다.
        fieldnames = reader.fieldnames
        # CSV의 각 행을 순회합니다.
        for row in reader:
            # 현재 행의 'user_id'가 명령어를 실행한 사용자의 'user_id'와 일치하는지 확인합니다.
            if row["user_id"] == user_id:
                submission_list.append(row)  # 일치하면 리스트에 추가합니다.

    # --- 필터링된 제출내역 존재 여부 확인 ---
    # 필터링된 'submission_list'가 비어있다면 (해당 사용자의 제출 내역이 없다면)
    if not submission_list:
        # 사용자 DM 채널에 해당 멤버의 제출내역이 없다는 메시지를 전송하고 함수를 종료합니다.
        client.chat_postMessage(
            channel=dm_channel_id, text="조회 멤버의 제출내역이 없습니다."
        )
        return None

    # --- 사용자의 제출내역을 CSV 파일로 임시 저장 후 전송 ---
    temp_dir = "data/temp"  # 임시 파일을 저장할 디렉토리 경로
    # 임시 디렉토리가 존재하지 않으면 생성합니다.
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 임시 CSV 파일의 경로를 정의합니다. 파일명은 사용자 ID를 포함합니다.
    temp_file_path = f"{temp_dir}/{user_id}.csv"
    # 임시 CSV 파일을 쓰기 모드('w')로 엽니다. 기존 파일이 있다면 덮어씁니다.
    with open(temp_file_path, "w", newline="") as csvfile:
        # 'csv.DictWriter'를 사용하여 헤더(fieldnames)와 딕셔너리 리스트를 CSV 파일로 작성합니다.
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()  # 헤더 행을 작성합니다.
        writer.writerows(submission_list)  # 필터링된 모든 제출 내역을 작성합니다.

    # 'client.files_upload_v2' API를 호출하여 생성된 임시 CSV 파일을 Slack에 업로드합니다.
    client.files_upload_v2(
        channel=dm_channel_id,  # 업로드할 채널 (사용자의 DM 채널)
        file=temp_file_path,    # 업로드할 파일 경로
        initial_comment=f"<@{user_id}> 님의 제출내역 입니다!",  # 파일과 함께 전송될 초기 코멘트
    )

    # --- 임시로 생성한 CSV 파일 삭제 ---
    # 파일 전송이 완료된 후, 임시 파일을 삭제합니다.
    os.remove(temp_file_path)


# Slack 슬래시 명령어 `/관리자`에 대한 핸들러 함수입니다.
# 관리자만 특정 메뉴를 조회하고 전체 제출내역을 가져올 수 있도록 합니다.
@app.command("/관리자")
def handle_some_command(ack, body, client: WebClient):
    # Slack 요청을 즉시 승인합니다.
    ack()

    # --- 관리자 권한 확인 ---
    # 명령어를 실행한 사용자의 ID를 추출합니다.
    user_id = body["user_id"]
    # 명령어가 실행된 채널 ID를 추출합니다.
    channel_id = body["channel_id"]
    
    # 관리자 ID(하드코딩된 "U08TDQNJE10")와 현재 사용자의 ID를 비교하여 관리자인지 확인합니다.
    if user_id != "U08TDQNJE10":
        # 관리자가 아닌 경우, 'chat_postEphemeral' API를 사용하여 요청한 사용자에게만 보이는 메시지를 전송합니다.
        # 이 메시지는 다른 채널 멤버에게는 보이지 않습니다. (Slack에서 '나에게만 표시' 문구로 출력됨)
        client.chat_postEphemeral(
            channel=body["channel_id"],  # 메시지를 보낼 채널
            user=user_id,               # 메시지를 볼 특정 사용자
            text="관리자만 사용 가능한 명령어입니다.",  # 보낼 메시지 텍스트
        )
        return None  # 관리자가 아니므로 함수를 종료합니다.

    # --- 관리자용 버튼 전송 (전체 제출내역 조회를 위한) ---
    # 관리자인 경우, 'chat_postEphemeral' API를 사용하여 관리자에게만 보이는 메시지와 함께 버튼을 전송합니다.
    client.chat_postEphemeral(
        channel=channel_id,
        user=user_id,
        text="관리자 메뉴를 선택해주세요.",
        blocks=[  # Block Kit을 사용하여 버튼을 포함한 블록을 정의합니다.
            {
                "type": "actions",  # 액션 블록 (버튼과 같은 상호작용 요소를 포함)
                "elements": [
                    {
                        "type": "button",  # 버튼 요소
                        "text": {
                            "type": "plain_text",
                            "text": "전체 제출내역 조회",
                            "emoji": True,
                        },
                        "value": "admin_value_1",  # 버튼 클릭 시 전달될 값
                        "action_id": "fetch_all_submission",  # 이 버튼과 연결될 액션 ID
                    }
                ],
            }
        ],
    )


# 'fetch_all_submission' 액션 ID를 가진 버튼이 클릭되었을 때 호출되는 핸들러 함수입니다.
# 이는 관리자 전용 메뉴에서 "전체 제출내역 조회" 버튼을 클릭했을 때 트리거됩니다.
@app.action("fetch_all_submission")
def handle_some_action(ack, body, client: WebClient):
    # Slack 요청을 즉시 승인합니다.
    ack()
    
    # --- 관리자의 DM 채널 ID 가져오기 ---
    # 액션을 트리거한 사용자의 ID를 추출합니다.
    user_id = body["user"]["id"]
    # 'client.conversations_open' API를 호출하여 관리자와의 DM 채널을 엽니다.
    response = client.conversations_open(users=user_id)
    # print(response) # 디버깅을 위한 출력 (선택 사항)
    # 응답에서 DM 채널의 ID를 추출합니다.
    dm_channel_id = response["channel"]["id"]

    # --- 전체 제출내역을 불러와서 전송 ---
    file_path = "data/db.csv"  # 전체 제출내역 CSV 파일 경로

    # CSV 파일이 존재하지 않는 경우 (제출된 내역이 없는 경우)
    if not os.path.exists(file_path):
        # 관리자 DM 채널에 제출내역이 없다는 메시지를 전송하고 함수를 종료합니다.
        client.chat_postMessage(
            channel=dm_channel_id,
            text="제출내역이 없습니다."
        )
        return None
    
    # 'client.files_upload_v2' API를 호출하여 'data/db.csv' 파일(전체 제출내역)을 Slack에 업로드합니다.
    client.files_upload_v2(
        channel=dm_channel_id,  # 업로드할 채널 (관리자의 DM 채널)
        file=file_path,         # 업로드할 파일 경로
        initial_comment="전체 제출내역 입니다!"  # 파일과 함께 전송될 초기 코멘트
    )


# 메인 실행 블록: 스크립트가 직접 실행될 때만 코드가 실행되도록 합니다.
if __name__ == "__main__":
    # Slack 소켓 모드 핸들러를 초기화합니다.
    # 'app' 인스턴스와 'SLACK_APP_TOKEN' 환경 변수를 사용하여 소켓 연결을 설정합니다.
    # 이 토큰은 앱 레벨의 토큰으로, 소켓 모드 연결을 인증하는 데 사용됩니다.
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    
    # 봇이 Slack과 소켓 모드 연결을 시작하고 이벤트를 수신 대기합니다.
    # 이 코드가 실행되면 봇은 활성 상태가 되어 Slack 이벤트에 응답할 수 있습니다.
    handler.start()
