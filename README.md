-----

슬랙 봇에 사용된 OAuth 권한(스코프) 리스트를 README 파일에 추가했습니다. 이제 봇이 어떤 권한을 필요로 하고, 각 권한이 어떤 역할을 하는지 쉽게 확인할 수 있습니다.

아래 업데이트된 README.md 파일을 확인해 주세요.

-----

# 🛠️ Python 가상환경 및 Slack Bot 프로젝트 설정 (README.md)

이 프로젝트는 Python 가상환경 설정을 통해 독립적인 개발 환경을 구축하고, Slack Bot을 개발하여 특정 채널에서 사용자 입력을 받고 CSV 파일로 데이터를 저장하며, 사용자별 또는 관리자용으로 데이터를 조회하는 기능을 구현합니다.

-----

### 📝 사전 준비: Python과 VS Code 설치

슬랙봇 프로젝트를 시작하기 전에 **Python**과 \*\*Visual Studio Code (VS Code)\*\*가 설치되어 있어야 합니다.

  * **Python:** 프로젝트를 실행하는 데 필요한 언어입니다.
      * [Python 공식 웹사이트](https://www.python.org/downloads/)에서 최신 버전을 다운로드하여 설치할 수 있습니다.
      * 설치 시 환경 변수(Path) 추가 옵션을 꼭 선택해 주세요.
  * **Visual Studio Code (VS Code):** 코드를 작성하고 관리하기 위한 편리한 통합 개발 환경(IDE)입니다.
      * [VS Code 공식 웹사이트](https://code.visualstudio.com/download)에서 다운로드하여 설치할 수 있습니다.

-----

### ✅ 1. 가상환경 생성

#### macOS / Linux

```bash
python3 -m venv ./
```

#### Windows

```bash
python -m venv .\
```

  * `venv`는 프로젝트마다 독립된 Python 실행 환경을 만드는 도구입니다.
  * `./` 또는 `.\`는 **현재 디렉토리**에 가상환경 폴더를 만든다는 뜻입니다.
  * 이 과정은 `bin/`, `Scripts/`, `lib/` 등의 폴더를 포함한 **가상환경 디렉토리 구조를 생성**합니다.

-----

### ✅ 2. 가상환경 활성화

#### macOS / Linux

```bash
source ./bin/activate
```

#### Windows

```bash
.\Scripts\activate
```

  * 가상환경을 **활성화(activate)** 하면 해당 프로젝트 전용의 Python 환경이 적용됩니다.
  * 이 상태에서는 `pip install` 등의 명령이 모두 **현재 가상환경 내에만 영향**을 미칩니다.
  * 프롬프트 앞에 `(venv)` 또는 `(env)` 와 같은 표시가 생깁니다.

-----

### ✅ 3. 필요한 패키지 설치

가상환경 활성화 후, 슬랙 봇 개발에 필요한 라이브러리를 설치합니다.

```bash
pip install slack_bolt python-dotenv
```

  * `slack_bolt`: Slack Bot을 개발하기 위한 공식 Python SDK입니다.
  * `python-dotenv`: `.env` 파일에 저장된 환경 변수를 코드에서 로드할 수 있도록 돕는 라이브러리입니다.

-----

### ✅ 4. `.env` 파일 설정 (환경 변수 관리)

`.env` 파일은 민감한 정보(API 키, 토큰 등)를 코드에 직접 노출하지 않고 관리하기 위한 파일입니다.

1.  **프로젝트 루트 디렉토리**에 `.env` 파일을 생성합니다.

2.  아래와 같이 Slack API에서 발급받은 토큰 정보를 입력합니다. (실제 값으로 대체해야 합니다.)

    ```
    SLACK_BOT_TOKEN=xoxb-YOUR_SLACK_BOT_TOKEN
    SLACK_APP_TOKEN=xapp-YOUR_SLACK_APP_TOKEN
    ```

      * **`SLACK_BOT_TOKEN`**: 봇 토큰 (시작: `xoxb-`)
      * **`SLACK_APP_TOKEN`**: 앱 토큰 (시작: `xapp-`)

3.  **Slack API 웹사이트**에서 `bot token`과 `app token`을 가져오고 환경 변수를 추가해야 합니다.
    링크: [https://api.slack.com/apps](https://api.slack.com/apps)

    *참고: `.env` 파일은 Git과 같은 버전 관리 시스템에 포함시키지 않도록 `.gitignore` 파일에 추가하는 것이 일반적입니다.*

-----

### ✅ 5. 설치된 패키지 목록 저장

현재 가상환경에 설치된 모든 패키지와 버전 정보를 `requirements.txt` 파일로 저장합니다.

```bash
pip freeze > requirements.txt
```

  * 다른 사람이 이 파일을 사용하면 **같은 환경을 그대로 재현**할 수 있습니다.
  * 협업 또는 배포 시 매우 중요합니다.

-----

### ✅ 6. `requirements.txt`로 패키지 재설치

`requirements.txt` 파일에 명시된 모든 패키지를 한 번에 설치합니다.

```bash
pip install -r requirements.txt
```

  * 팀 프로젝트나 서버 배포 시 **환경을 일관되게 유지**하는 데 필수적입니다.

-----

### ✅ 7. 가상환경 비활성화

```bash
deactivate
```

  * 현재 활성화된 가상환경을 종료하고 시스템 기본 Python 환경으로 돌아갑니다.
  * 다른 프로젝트 작업 시 충돌을 방지하기 위해 반드시 비활성화해야 합니다.

-----

### 📌 Slack Bot 주요 기능 요약

이 Slack Bot은 사용자 상호작용 및 데이터 관리를 위한 다음 세 가지 주요 명령어를 제공합니다.

#### 1\. 데이터 수집하기 (`/제출` 명령어)

  * 문장을 제출하는 데 사용하는 `/제출` 명령어 설정
  * 명령어를 수신 받을 수 있는 `command` 함수 추가
  * 수집할 데이터 항목(제목, 컨텐츠, 의견)을 입력할 수 있는 모달 창 띄우기
  * 사용자의 데이터 입력 및 제출 처리

#### 2\. 데이터 저장하기 (`/제출` 명령어 후속 처리)

  * 모달 데이터를 전달 받는 `view` 함수 추가
  * 문장 제출이 가능한 채널인지 검증 (validation)
  * 제출한 문장이 3글자 이상인지 검증 (validation)
  * 모달 폼에서 저장할 데이터(사용자 ID, 사용자 이름, 제목, 컨텐츠, 의견, 제출일시) 추출
  * 파일 시스템을 이용한 데이터 저장 (`data/db.csv` 파일에 CSV 형식으로 저장)
  * 제출 완료 후 채널에 완료 메시지 전송

#### 3\. 데이터 가져오기 (`/조회` 명령어)

  * 제출 내역을 조회하는 데 사용하는 `/조회` 명령어 설정
  * 명령어를 수신 받을 수 있는 `command` 함수 추가
  * 제출 내역이 존재하지 않는(아무도 제출한 적이 없는) 경우 적절한 메시지를 전송 후 종료
  * 명령어를 사용한 멤버의 DM 채널 ID 가져오기
  * 멤버의 제출 내역 필터링 (해당 멤버의 제출 내역이 없다면 적절한 메시지 전송 후 종료)
  * 멤버의 제출 내역을 포함하는 임시 CSV 파일 생성
  * 멤버 DM 채널로 임시 제출 내역 파일 전송
  * 임시 제출 내역 파일 삭제 (전송 완료 후)

#### 4\. 어드민 전용 모드 (`/관리자` 명령어)

  * 관리자 메뉴를 호출하는 `/관리자` 명령어 설정
  * 명령어를 사용한 사용자가 관리자 ID인지 확인 후, 관리자가 아닌 경우 '나에게만 표시'되는 메시지 전송
  * 관리자용 버튼(예: '전체 제출내역 조회')이 포함된 메시지 전송
  * 버튼 '전체 제출내역 조회'에 대한 `action` 함수 추가
  * 관리자 DM 채널로 전체 제출 내역 파일(`data/db.csv`) 반환

-----

### 📌 Slack Bot 기능 상세 설명 및 JSON 예시

이 Slack Bot은 `/제출`, `/조회`, `/관리자` 세 가지 명령어를 통해 작동하며, 사용자 상호작용 및 데이터 관리를 지원합니다. 각 기능에서 Slack API를 통해 수신하는 주요 `body` JSON 데이터의 예시를 함께 제시하여 동작 방식을 더 명확히 이해할 수 있습니다.

-----

#### 1\. `/제출` 명령어: 데이터 제출 및 저장

사용자가 Slack 채널에 `/제출` 명령어를 입력하면, 봇은 데이터를 입력받을 수 있는 **모달 폼**을 띄웁니다.

  * **명령어**: `/제출`

  * **`@app.command("/제출")` 수신 `body` JSON 예시**:

    ```json
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
        "trigger_id": "9085180778055.8931838625970.032aefbbce14bbf4dcb21f7b0ae4f540"
    }
    ```

    *설명: 위 `body`는 사용자가 `/제출` 명령어를 입력했을 때 Slack에서 봇으로 전송되는 데이터입니다. `trigger_id`를 사용하여 모달을 열 수 있습니다.*

  * **동작 방식**:

      * 명령어 입력 시, `app.command("/제출")` 핸들러가 트리거되어 **제목, 컨텐츠, 의견**을 입력할 수 있는 모달 폼을 엽니다.
      * 사용자가 모달 폼을 \*\*제출(Submit)\*\*하면 `app.view("submit_view")` 핸들러가 호출됩니다.

  * **`@app.view("submit_view")` 수신 `body` JSON 예시**:

    ```json
    {
        "type": "view_submission",
        "team": {"id": "T08TDQNJDUJ", "domain": "qhdltmwhs"},
        "user": {
            "id": "U08TDQNJE10",
            "username": "qhdltmwhs",
            "name": "qhdltmwhs",
            "team_id": "T08TDQNJDUJ"
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
                    "label": {"type": "plain_text", "text": "제목", "emoji": true},
                    "optional": false,
                    "dispatch_action": false,
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "input_action_id",
                        "placeholder": {"type": "plain_text", "text": "뉴진스", "emoji": true},
                        "multiline": false,
                        "dispatch_action_config": {"trigger_actions_on": ["on_enter_pressed"]}
                    }
                },
                {
                    "type": "input",
                    "block_id": "contents_block_id",
                    "label": {"type": "plain_text", "text": "컨텐츠", "emoji": true},
                    "optional": false,
                    "dispatch_action": false,
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "input_action_id",
                        "placeholder": {"type": "plain_text", "text": "강해린", "emoji": true},
                        "multiline": true,
                        "dispatch_action_config": {"trigger_actions_on": ["on_enter_pressed"]}
                    }
                },
                {
                    "type": "input",
                    "block_id": "comment_block_id",
                    "label": {"type": "plain_text", "text": "의견", "emoji": true},
                    "optional": true,
                    "dispatch_action": false,
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "input_action_id",
                        "placeholder": {"type": "plain_text", "text": "최애 걸그룹 멤버", "emoji": true},
                        "multiline": true,
                        "dispatch_action_config": {"trigger_actions_on": ["on_enter_pressed"]}
                    }
                }
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
                        "input_action_id": {"type": "plain_text_input", "value": "걸그룹 멤버"}
                    }
                }
            },
            "hash": "1750823284.P0IHmfHd",
            "title": {"type": "plain_text", "text": "모달 폼 테스트", "emoji": true},
            "clear_on_close": false,
            "notify_on_close": false,
            "close": {"type": "plain_text", "text": "취소", "emoji": true},
            "submit": {"type": "plain_text", "text": "제출", "emoji": true},
            "previous_view_id": null,
            "root_view_id": "V092S1M0RSA",
            "app_id": "A092UFX0E4A",
            "external_id": "",
            "app_installed_team_id": "T08TDQNJDUJ",
            "bot_id": "B092MNXLW1H"
        },
        "response_urls": [],
        "is_enterprise_install": false,
        "enterprise": null
    }
    ```

    *설명: 위 `body`는 사용자가 모달 폼에 데이터를 입력하고 제출 버튼을 눌렀을 때 Slack에서 봇으로 전송되는 데이터입니다. `view.state.values`를 통해 입력된 값을 추출할 수 있습니다.*

  * **`client.users_info()` 응답 JSON 예시**:

    ```json
    {
        "ok": true,
        "user": {
            "id": "U08TDQNJE10",
            "name": "qhdltmwhs",
            "is_bot": false,
            "updated": 1748325557,
            "is_app_user": false,
            "team_id": "T08TDQNJDUJ",
            "deleted": false,
            "color": "902d59",
            "is_email_confirmed": true,
            "real_name": "모네",
            "tz": "Asia/Seoul",
            "tz_label": "Korea Standard Time",
            "tz_offset": 32400,
            "is_admin": true,
            "is_owner": true,
            "is_primary_owner": true,
            "is_restricted": false,
            "is_ultra_restricted": false,
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
                "is_custom_image": true,
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
                "status_expiration": 0
            }
        }
    }
    ```

    *설명: `client.users_info()` 호출 시 반환되는 사용자 정보입니다. `user.real_name`을 통해 사용자의 실제 이름을 얻을 수 있습니다.*

  * **유효성 검사**:

      * **채널 검증**: 모달 폼에 저장된 `private_metadata` (명령어 입력 시의 `channel_id`)를 사용하여, 제출이 **`C08TJM1RG2E` (test)** 채널에서만 이루어졌는지 확인합니다. 다른 채널에서 제출 시, `response_action="errors"`를 통해 **컨텐츠 입력 필드에 "해당 채널에서만 제출할 수 있습니다."** 라는 오류 메시지를 표시합니다.
      * **글자 수 검증**: 입력된 컨텐츠의 길이가 3글자 미만인 경우, **컨텐츠 입력 필드에 "컨텐츠는 세 글자 이상 입력해주세요."** 라는 오류 메시지를 표시합니다.

  * **데이터 저장**:

      * 유효성 검사를 통과하면, 사용자 ID, 사용자 이름, 제목, 컨텐츠, 의견, 제출 일시(`YYYY-MM-DD HH:MM:SS` 형식)를 추출합니다.
      * 이 데이터는 `data/db.csv` 파일에 **CSV 형식**으로 추가 저장됩니다. `data` 디렉터리가 없으면 자동으로 생성됩니다. 파일이 비어있는 경우 헤더 행이 자동으로 추가됩니다.

  * **완료 메시지**: 데이터 저장 후, 제출이 성공적으로 완료되었음을 알리는 메시지가 원래 제출이 이루어진 Slack 채널에 게시됩니다. (`<@{user_id}> 님이 {title}의 {contents}에 대해 {comment} 의견 공유`)

-----

#### 2\. `/조회` 명령어: 개인 제출 내역 조회

사용자가 자신의 과거 제출 내역을 CSV 파일로 받고 싶을 때 사용하는 명령어입니다.

  * **명령어**: `/조회`
  * **`@app.command("/조회")` 수신 `body` JSON 예시**:
      * `/제출` 명령어의 `body` JSON 구조와 유사하며, `command` 필드만 `/조회`로 변경됩니다. ( 섹션의 `@app.command` 예시 참고)
  * **동작 방식**:
      * 명령어 입력 시 `app.command("/조회")` 핸들러가 호출됩니다.
      * **개인 DM 채널**을 열어 해당 채널로 응답을 보낼 준비를 합니다.
  * **제출 내역 확인 및 전송**:
      * `data/db.csv` 파일이 존재하지 않는 경우, 사용자 DM 채널에 "전체 멤버의 제출내역이 없습니다." 메시지를 보냅니다.
      * `db.csv` 파일에서 명령어를 입력한 `user_id`에 해당하는 제출 내역만 필터링합니다.
      * 필터링된 제출 내역이 없는 경우, DM 채널에 "조회 멤버의 제출내역이 없습니다." 메시지를 보냅니다.
      * 제출 내역이 있다면, 해당 내역을 포함하는 임시 CSV 파일(`data/temp/{user_id}.csv`)을 생성합니다.
      * 생성된 CSV 파일을 사용자 DM 채널로 업로드하며, `<@{user_id}> 님의 제출내역 입니다!`라는 초기 코멘트를 함께 보냅니다.
  * **임시 파일 관리**: 파일 전송이 완료되면 보안 및 공간 관리를 위해 임시 생성된 CSV 파일은 자동으로 삭제됩니다.

-----

#### 3\. `/관리자` 명령어: 관리자 전용 기능

이 명령어는 특정 관리자만 사용할 수 있으며, 전체 제출 내역을 조회하는 기능을 제공합니다.

  * **명령어**: `/관리자`

  * **`@app.command("/관리자")` 수신 `body` JSON 예시**:

      * `/제출` 명령어의 `body` JSON 구조와 유사하며, `command` 필드만 `/관리자`로 변경됩니다. ([1. `/제출` 명령어] 섹션의 `@app.command` 예시 참고)

  * **동작 방식**:

      * 명령어 입력 시 `app.command("/관리자")` 핸들러가 호출됩니다.

  * **관리자 검증**:

      * 명령어를 실행한 `user_id`가 코드에 하드코딩된 관리자 ID (`U08TDQNJE10`)와 일치하는지 확인합니다.
      * 관리자가 아닌 경우, 해당 사용자에게만 **Ephemeral 메시지**로 "관리자만 사용 가능한 명령어입니다."를 표시합니다. (다른 사용자에게는 보이지 않음)

  * **관리자 메뉴**:

      * 관리자에게는 "관리자 메뉴를 선택해주세요."라는 메시지와 함께 **"전체 제출내역 조회" 버튼**이 포함된 임시 메시지가 전송됩니다.
      * (참고 링크 : [https://app.slack.com/block-kit-builder](https://app.slack.com/block-kit-builder))

  * **`@app.action("fetch_all_submission")` 수신 `body` JSON 예시**:

    ```json
    {
        "type": "block_actions",
        "user": {
            "id": "U08TDQNJE10",
            "username": "qhdltmwhs",
            "name": "qhdltmwhs",
            "team_id": "T08TDQNJDUJ"
        },
        "api_app_id": "A092UFX0E4A",
        "token": "lTJNImiDDZe6kNQuqABlYDAe",
        "container": {
            "type": "message",
            "message_ts": "1750855711.001000",
            "channel_id": "C08TJM1RG2E",
            "is_ephemeral": true
        },
        "trigger_id": "9095272100611.8931838625970.9fc649307ba6dd73fdd98443b1e7c8c8",
        "team": {"id": "T08TDQNJDUJ", "domain": "qhdltmwhs"},
        "enterprise": null,
        "is_enterprise_install": false,
        "channel": {"id": "C08TJM1RG2E", "name": "test"},
        "state": {"values": {}},
        "response_url": "https://hooks.slack.com/actions/T08TDQNJDUJ/9095272082035/6TOsbTHTPGnq6ZqYzJDhtVzt",
        "actions": [
            {
                "action_id": "fetch_all_submission",
                "block_id": "4N7BG",
                "text": {"type": "plain_text", "text": "전체 제출내역 조회", "emoji": true},
                "value": "admin_value_1",
                "type": "button",
                "action_ts": "1750855713.631129"
            }
        ]
    }
    ```

    *설명: 위 `body`는 관리자 메뉴에서 "전체 제출내역 조회" 버튼을 클릭했을 때 Slack에서 봇으로 전송되는 데이터입니다. `actions` 배열에서 어떤 버튼이 클릭되었는지 확인할 수 있습니다.*

  * **전체 제출내역 조회 (`fetch_all_submission` 액션)**:

      * 관리자가 "전체 제출내역 조회" 버튼을 클릭하면 `app.action("fetch_all_submission")` 핸들러가 호출됩니다.
      * 관리자의 **개인 DM 채널**을 열고, `data/db.csv` 파일(전체 제출 내역)을 해당 채널로 업로드합니다.
      * `db.csv` 파일이 존재하지 않는 경우, "제출내역이 없습니다." 메시지를 보냅니다.
      * 파일 업로드 시 "전체 제출내역 입니다\!"라는 초기 코멘트가 함께 전송됩니다.

-----

### 🔑 Slack 봇 OAuth 권한 (Scopes)

Slack 앱의 기능과 접근 권한은 요청하는 스코프(Scope)에 따라 결정됩니다. `Bot`에 사용된 봇 토큰 스코프는 다음과 같습니다.

| OAuth Scope           | 설명                                                     |
| :-------------------- | :------------------------------------------------------- |
| `channels:history`    | `Bot`이 추가된 **공개 채널**의 메시지 및 기타 콘텐츠 조회 |
| `channels:write.invites` | **공개 채널**에 멤버 초대                                |
| `channels:write.topic` | **공개 채널**의 설명을 설정                                |
| `chat:write`          | `@Bot` 이름으로 메시지 전송                          |
| `commands`            | 사용자가 사용할 수 있는 **단축키 및 슬래시 명령어** 추가 |
| `files:write`         | `Bot` 이름으로 파일 업로드, 편집, 삭제               |
| `groups:write`        | `Bot`이 추가된 **비공개 채널** 관리 및 새 채널 생성  |
| `im:history`          | `Bot`이 추가된 \*\*DM(다이렉트 메시지)\*\*의 메시지 및 기타 콘텐츠 조회 |
| `im:write`            | 사용자와 **DM** 시작                                     |
| `mpim:write`          | **그룹 DM** 시작                                         |
| `users:read`          | 워크스페이스 내 사용자 조회                              |

-----

### 📌 Slack Bot 개발 및 실행

  * **SlackBolt 개발 문서 확인**: Slack Bot 개발을 위한 더 자세한 내용은 공식 문서를 참조하세요.
    링크: [https://slack.dev/bolt-python/concepts](https://slack.dev/bolt-python/concepts)

  * **SlackBolt 코드 작성**: `SLACK_BOT_TOKEN`과 `SLACK_APP_TOKEN` 환경 변수를 사용하여 Slack 봇 코드를 작성합니다. `.env` 파일에서 환경 변수를 로드하려면 코드 상단에 다음을 추가해야 합니다.

    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv() # .env 파일에서 환경 변수를 로드합니다.

    # 환경 변수 사용 예시:
    # bot_token = os.getenv("SLACK_BOT_TOKEN")
    # app_token = os.getenv("SLACK_APP_TOKEN")

    # 이후 Slack Bolt 앱 초기화 코드 작성
    ```

  * **봇 실행**: 프로젝트 루트 디렉토리에서 다음 명령어를 실행하여 봇을 시작합니다.

    ```bash
    python main.py
    ```

      * 이 명령은 **소켓 모드**를 통해 로컬에서 봇을 실행합니다. 봇 코드에 따라 `handler.start()`와 같은 명령을 사용합니다.

  * **슬랙 워크스페이스에서 봇에게 메시지 전송**: 봇이 성공적으로 실행되면, 해당 봇이 추가된 슬랙 워크스페이스에서 봇에게 직접 메시지를 보내거나 봇이 참여하고 있는 채널에서 메시지를 보내 봇의 동작을 테스트할 수 있습니다.

<!-- end list -->

```
```