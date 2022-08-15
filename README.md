## 起動方法
1. docker compose up --build
1. ブラウザでlocalhost:80にアクセス


## AIお試し方法
```python
from face_detector import YoloDetector
import numpy as np
from PIL import Image

model = YoloDetector(target_size=720,gpu=0,min_face=90)
orgimg = np.array(Image.open('test.jpeg'))
bboxes,points = model.predict(orgimg)
```

## 説明
- AI関連のライブラリのインポートが結構時間かかります。
- python3 crud.pyをすればデフォルトの画像でデータが作られ，DBに登録されます。
- python3 ai.pyを実行すればai.pyの挙動がわかります。
