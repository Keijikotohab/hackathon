# 導入方法
## 1. SlackBot作成
1. "https://api.slack.com/apps?new_app=1&manifest_json={%20%22display_information%22:%20{%20%22name%22:%20%22MonoOboe%22%20},%20%22features%22:%20{%20%22bot_user%22:%20{%20%22display_name%22:%20%22MonoOboe%22,%20%22always_online%22:%20false%20}%20},%20%22oauth_config%22:%20{%20%22scopes%22:%20{%20%22bot%22:%20[%20%22channels:history%22,%20%22channels:read%22,%20%22chat:write%22,%20%22chat:write.public%22,%20%22files:write%22,%20%22groups:read%22,%20%22im:history%22,%20%22im:read%22,%20%22im:write%22,%20%22mpim:read%22,%20%22reactions:write%22,%20%22users:read%22,%20%22reactions:read%22%20]%20}%20},%20%22settings%22:%20{%20%22org_deploy_enabled%22:%20false,%20%22socket_mode_enabled%22:%20false,%20%22token_rotation_enabled%22:%20false%20}%20}"
1. 自分のワークスペースを選んで次へ
1. `install to Workspace`
1. `Allow`
1. `App Home` > `Allow users to send Slash commands and messages from the messages tab`をチェック
1. `Oauth&Permission` > `Bot User OAuth Token`をコピー

## 2. .envファイルの作成
1. ディレクトリに，`.env`を作成
1. `.env`に先ほどコピーしたtokenを貼り付け
```python:.env
SLACK_TOKEN={Here change bot token, and delete "{}"}
SLACK_CHANNEL_ID={Here change channel id, and delete "{}"}
```
## 3. サーバー起動
1. `cd backend`
1. `docker compose up --build`

## 4. アプリアクセス
- `http://localhost:3000`にアクセス
