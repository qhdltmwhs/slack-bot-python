import os
import csv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from datetime import datetime
from slack_sdk import WebClient

load_dotenv()

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])


# Add middleware / listeners here

# This will match any message that contains 👋
# @app.message("ㅎㅇ")
# def say_hello(message, say):
#     user = message["user"]
#     # print(user)
#     say(f"Hi there, <@{user}>!")


# @app.command - body json result e.g. : 실제 코드와 무관
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


# @app.view - body json result e.g. : 실제 실행 코드와 무관
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

# @app.view - client.users_info(user=body["user"]["id"]) json result e.g. : 실제 실행 코드와 무관
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


# @app.action("fetch_all_submission") - body json result e.g. : 실제 실행 코드와 무관
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


@app.command("/제출")
def handle_submit_command(ack, body, client):
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            "callback_id": "submit_view",
            # private_metadata 값 활용 = app.view 의 바디 결과에 채널 정보 같은게 없어서 여기서 미리 넣어서 전달 가능 *중요*!
            "private_metadata": body["channel_id"],
            "title": {"type": "plain_text", "text": "모달 폼 테스트"},
            "close": {"type": "plain_text", "text": "취소"},
            "submit": {"type": "plain_text", "text": "제출"},
            "blocks": [
                # {
                #     "type": "section",
                #     "text": {
                #         "type": "mrkdwn",
                #         "text": "Welcome to a modal with _blocks_",
                #     },
                #     "accessory": {
                #         "type": "button",
                #         "text": {"type": "plain_text", "text": "Click me!"},
                #         "action_id": "button_abc",
                #     },
                # },
                {
                    "type": "input",
                    "block_id": "title_block_id",
                    "label": {
                        "type": "plain_text",
                        "text": "제목",
                    },
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "input_action_id",
                        "multiline": False,
                        "placeholder": {"type": "plain_text", "text": "뉴진스"},
                    },
                },
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
                        "multiline": True,
                        "placeholder": {"type": "plain_text", "text": "강해린"},
                    },
                },
                {
                    "type": "input",
                    "block_id": "comment_block_id",
                    "optional": True,  # 필수가 아님 여부
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


# @app.command("/제출") "callback_id": "submit_view"의 값과 app.view("submit_view") 인자 값 일치 (설정 가능)
@app.view("submit_view")
def handle_view_submission_events(ack, body, client):

    # 제출 가능한 채널인지 유효성 검사
    channel_id = body["view"]["private_metadata"]
    if channel_id != "C08TJM1RG2E":
        ack(
            response_action="errors",
            # "contents_block_id" = 모달폼에서 지정한 입력 창에 해당 메시지 띄우기
            errors={"contents_block_id": "#test 채널에서만 제출할 수 있습니다."},
        )
        return None

    # 제출 가능한 글자수 유효성 검사
    contents = body["view"]["state"]["values"]["contents_block_id"]["input_action_id"][
        "value"
    ]
    if len(contents) < 3:
        ack(
            response_action="errors",
            # "contents_block_id" = 모달폼에서 지정한 입력 창에 해당 메시지 띄우기
            errors={"contents_block_id": "컨텐츠는 세 글자 이상 입력해주세요."},
        )
        return None
    # Slack의 상호작용(Interactivity) 요청, 특히 모달(Modal)이나 단축키(Shortcuts),
    # 대화형 구성 요소(Interactive Components)와 같이 사용자 액션에 대한 즉각적인 응답이 필요한 경우에 사용됩니다.
    ack()

    # 저장할 데이터
    # 멤버 정보
    user_id = body["user"]["id"]
    user_info = client.users_info(user=user_id)
    user_name = user_info["user"]["real_name"]
    # 제목
    title = body["view"]["state"]["values"]["title_block_id"]["input_action_id"][
        "value"
    ]
    # 컨텐츠
    contents = body["view"]["state"]["values"]["contents_block_id"]["input_action_id"][
        "value"
    ]
    # 의견
    comment = body["view"]["state"]["values"]["comment_block_id"]["input_action_id"][
        "value"
    ]
    # 생성일시
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # data 디렉토리가 없다면 생성
    if not os.path.exists("data"):
        os.makedirs("data")

    # 제출 정보를 CSV 파일에 저장
    with open("data/db.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # 파일 사이즈가 0 이하면 헤더 행 추가
        if not os.path.getsize("data/db.csv") > 0:
            writer.writerow(
                ["user_id", "user_name", "title", "contents", "comment", "created_at"]
            )

        writer.writerow([user_id, user_name, title, contents, comment, created_at])

    # 슬랙 채널에 완료 안내 메시지 보내기
    # <@{user_id}> 슬랙에서 멘션 효과
    text = f">>> *<@{user_id}>님이 `{title}`의 *\n\n '{contents}'에 대해 \n"
    if comment:
        text += f"\n {comment} 의견 공유 \n"
    client.chat_postMessage(channel=channel_id, text=text)


@app.command("/조회")
def handle_submission_history_command(ack, body, client: WebClient):
    ack()

    # 멤버의 DM 채널 ID 가져오기
    user_id = body["user_id"]
    response = client.conversations_open(users=user_id)
    dm_channel_id = response["channel"]["id"]

    # 만약에 제출내역 파일이 없다면 제출내역이 없다고 메시지를 전송하고 종료
    if not os.path.exists("data/db.csv"):
        client.chat_postMessage(
            channel=dm_channel_id, text="전체 멤버의 제출내역이 없습니다."
        )
        return None

    # 멤버의 제출내역만 필터링
    submission_list = []
    with open("data/db.csv") as csvfile:
        # csv.DictReader가 CSV의 첫행을 헤더의 키로 사용하여 각 행을 딕셔너리로 만들어준다는 점 참고!
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        for row in reader:
            if row["user_id"] == user_id:
                submission_list.append(row)

    # print(submission_list)

    # 만약에 제출내역이 없다면 제출내역이 없다고  메시지를 전송하고 종료
    if not submission_list:
        client.chat_postMessage(
            channel=dm_channel_id, text="조회 멤버의 제출내역이 없습니다."
        )
        return None

    # 사용자의 제출내역을 CSV 파일로 임시 저장 후 전송
    temp_dir = "data/temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    temp_file_path = f"{temp_dir}/{user_id}.csv"
    # (temp_file_path, "w", newline="") 여기서 "w" = 덮어쓰기
    with open(temp_file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerows(submission_list)

    client.files_upload_v2(
        channel=dm_channel_id,
        file=temp_file_path,
        initial_comment=f"<@{user_id}> 님의 제출내역 입니다!",
    )

    # 임시로 생성한 CSV 파일을 삭제
    os.remove(temp_file_path)


@app.command("/관리자")
def handle_some_command(ack, body, client: WebClient):
    ack()

    # 관리자인지 확인 후  아니라면 메시지 전송 후 종료
    user_id = body["user_id"]
    channel_id = body["channel_id"]
    if user_id != "U08TDQNJE10":
        # chat_postEphemeral() 이 경우 커맨트 명령을 요청한 멤버에게만 메시지가 보이게 답장이 간다. (슬랙에서는 '나에게만 표시' 문구 출력)
        client.chat_postEphemeral(
            channel=body["channel_id"],
            user=user_id,
            text="관리자만 사용 가능한 명령어입니다.",
        )
        return None

    # 관리자용 버튼 전송(전체 제출내역을 반환)
    client.chat_postEphemeral(
        channel=channel_id,
        user=user_id,
        text="관리자 메뉴를 선택해주세요.",
        blocks=[
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "전체 제출내역 조회",
                            "emoji": True,
                        },
                        "value": "admin_value_1",
                        "action_id": "fetch_all_submission",
                    }
                ],
            }
        ],
    )


@app.action("fetch_all_submission")
def handle_some_action(ack, body, client: WebClient):
    ack()
    # 관리자의 DM 채널 ID 가져오기
    user_id = body["user"]["id"]
    response = client.conversations_open(users=user_id)
    dm_channel_id = response["channel"]["id"]

    # 전체 제출내역을 불러와서 전송
    file_path = "data/db.csv"

    if not os.path.exists(file_path):
        client.chat_postMessage(channel=dm_channel_id, text="제출내역이 없습니다.")
        return None

    client.files_upload_v2(
        channel=dm_channel_id, file=file_path, initial_comment="전체 제출내역 입니다!"
    )


if __name__ == "__main__":
    # export SLACK_APP_TOKEN=xapp-***
    # export SLACK_BOT_TOKEN=xoxb-***
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
