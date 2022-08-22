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

## ボット導入URl
- "https://api.slack.com/apps?new_app=1&manifest_yaml=display_information:%20name:%20NagosugiBot%20features:%20bot_user:%20display_name:%20NagosugiBot%20always_online:%20false%20oauth_config:%20scopes:%20bot:%20-%20channels:history%20-%20chat:write%20-%20chat:write.public%20-%20files:write%20-%20im:history%20-%20im:write%20-%20users:read%20-%20groups:read%20-%20mpim:read%20-%20im:read%20-%20channels:read%20settings:%20org_deploy_enabled:%20false%20socket_mode_enabled:%20false%20token_rotation_enabled:%20false" 
