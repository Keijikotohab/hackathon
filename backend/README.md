## 起動方法
1. docker compose up --build
1. ブラウザでlocalhost:80にアクセス

## 説明
- AI関連のライブラリのインポートが結構時間かかります。
- sqlite.pyを実行すればDBがリセットされ,ダミーデータが作られます。
- crud.pyを実行すればデフォルトの画像(test.jpeg)でデータが作られ，DBに登録されます。
        - 実行すると，dbの中身を全て消すようになっています。
        - そもそも，実行を想定していないからです。
- ai.pyを実行すればai.pyの挙動がなんとなくわかります。
        - 顔の切り取りは未実装
        - 画像をそのまま返している
- 画像はUUIDで管理するようにした。
        - UUIDと画像，UUIDと名前のペアを作って通信すれば紐づけられそう

## AIお試し方法
```python
from face_detector import YoloDetector
import numpy as np
from PIL import Image

model = YoloDetector(target_size=720,gpu=-1,min_face=90)
orgimg = np.array(Image.open('test.jpeg'))
bboxes,points = model.predict(orgimg)
```

# 導入方法
## SlackBot作成
1. "https://api.slack.com/apps?new_app=1&manifest_json={%20%22display_information%22:%20{%20%22name%22:%20%22MonoOboe%22%20},%20%22features%22:%20{%20%22bot_user%22:%20{%20%22display_name%22:%20%22MonoOboe%22,%20%22always_online%22:%20false%20}%20},%20%22oauth_config%22:%20{%20%22scopes%22:%20{%20%22bot%22:%20[%20%22channels:history%22,%20%22channels:read%22,%20%22chat:write%22,%20%22chat:write.public%22,%20%22files:write%22,%20%22groups:read%22,%20%22im:history%22,%20%22im:read%22,%20%22im:write%22,%20%22mpim:read%22,%20%22reactions:write%22,%20%22users:read%22,%20%22reactions:read%22%20]%20}%20},%20%22settings%22:%20{%20%22org_deploy_enabled%22:%20false,%20%22socket_mode_enabled%22:%20false,%20%22token_rotation_enabled%22:%20false%20}%20}"
1. 自分のワークスペースを選んで次へ
1. `install to Workspace`
1. `Allow`
1. `App Home` > `Allow users to send Slash commands and messages from the messages tab`をチェック
1. `Oauth&Permission` > `Bot User OAuth Token`をコピー

## .envファイルの作成
1. ディレクトリに，`.env`を作成
1. `.env`に先ほどコピーしたtokenを貼り付け
```python
SLACK_TOKEN={Here change bot token, end delete "{}"}
```
## サーバー起動
1. `docker compose up --build`
