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

## AIお試し方法
```python
from face_detector import YoloDetector
import numpy as np
from PIL import Image

model = YoloDetector(target_size=720,gpu=-1,min_face=90)
orgimg = np.array(Image.open('test.jpeg'))
bboxes,points = model.predict(orgimg)
```
