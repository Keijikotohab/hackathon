[![GitHub license](https://img.shields.io/github/license/Keijikotohab/hackathon?style=for-the-badge)](https://github.com/Keijikotohab/hackathon/blob/main/LICENSE)
![Lines of code](https://img.shields.io/tokei/lines/github/Keijikotohab/hackathon?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Keijikotohab/hackathon?style=for-the-badge)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Keijikotohab/hackathon?display_name=tag&style=for-the-badge)
[![GitHub stars](https://img.shields.io/github/stars/Keijikotohab/hackathon?style=for-the-badge)](https://github.com/Keijikotohab/hackathon/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Keijikotohab/hackathon?style=for-the-badge)](https://github.com/Keijikotohab/hackathon/network)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/Keijikotohab/hackathon?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/Keijikotohab/hackathon?style=for-the-badge)
![Twitter Follow](https://img.shields.io/twitter/follow/Mono_Oboe?style=for-the-badge)
[![Twitter](https://img.shields.io/twitter/url?style=for-the-badge&url=https%3A%2F%2Ftwitter.com%2FMono_Oboe)](https://twitter.com/intent/tweet?text=これは覚えられるわあ:&url=https%3A%2F%2Fgithub.com%2FKeijikotohab%2Fhackathon)

# モノオボエ導入方法
![haikeiarimono_1](https://user-images.githubusercontent.com/62993486/187008580-935290c9-c934-4363-8888-c9ae5b4e559d.png)

## 1. SlackBot作成
1. 次のURLをクリックしてボットを作成する。"https://api.slack.com/apps?new_app=1&manifest_json={%20%22display_information%22:%20{%20%22name%22:%20%22MonoOboe%22%20},%20%22features%22:%20{%20%22bot_user%22:%20{%20%22display_name%22:%20%22MonoOboe%22,%20%22always_online%22:%20false%20}%20},%20%22oauth_config%22:%20{%20%22scopes%22:%20{%20%22bot%22:%20[%20%22channels:history%22,%20%22channels:read%22,%20%22chat:write%22,%20%22chat:write.public%22,%20%22files:write%22,%20%22groups:read%22,%20%22im:history%22,%20%22im:read%22,%20%22im:write%22,%20%22mpim:read%22,%20%22reactions:write%22,%20%22users:read%22,%20%22reactions:read%22%20]%20}%20},%20%22settings%22:%20{%20%22org_deploy_enabled%22:%20false,%20%22socket_mode_enabled%22:%20false,%20%22token_rotation_enabled%22:%20false%20}%20}"
1. 自分のワークスペースを選んで次へ
1. `install to Workspace`
1. `Allow`
1. `App Home` > `Allow users to send Slash commands and messages from the messages tab`をチェック
1. `Oauth&Permission` > `Bot User OAuth Token`をコピー

## 2. .envファイルの作成
1. backendディレクトリに，`.env`を作成
1. `.env`に先ほどコピーしたtokenを貼り付け
1. `.env`に，slackチャンネルのIDを貼り付け
1. `.env`に，ボットとのDMチャンネルのIDを貼り付け
```python:.env
SLACK_TOKEN={Here change bot token, and delete "{}"}
SLACK_CHANNEL_ID={Here change channel id, and delete "{}"}
SLACK_USER_CHANNEL_ID={Here change user channel id between MonoOboe, and delete "{}"}
```
## 3. サーバー起動
1. `cd Docker`
1. `docker compose up --build`

## 4. アプリアクセス
- `http://localhost:3000`にアクセス
