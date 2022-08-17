import logging
from uuid import uuid4

import numpy as np
from PIL import Image

from face_detector import YoloDetector

logger = logging.getLogger("mylog")
logger.setLevel(logging.DEBUG)


class FaceDetector:
    """
    AIの力で写真から顔を切り抜く
    """

    def __init__(self, img_path: str):
        self.model = YoloDetector(target_size=360, gpu=-1, min_face=90)
        # pathじゃなくて，配列にするかも
        self.orgimg = np.array(Image.open(img_path))
        self.bboxes: list = list()
        logging.debug("model loaded")

    def predict(self):
        """
        ファイルパスにするためのuuidと，bboxのセットを作る
        """
        bboxes, points = self.model.predict(self.orgimg)
        self.bboxes = [[str(uuid4()), bbox] for bbox in bboxes[0]]

    ## Re-Develop ME
    def clip(self) -> list:
        """
        bboxの情報をもとに，写真を切り抜く。
        return [切り抜いた写真, uuid, bbox]
        """
        return [[self.orgimg, bbox[0], bbox[1]] for bbox in self.bboxes]


if __name__ == "__main__":
    fd = FaceDetector("test.jpeg")
    fd.predict()
    ret = fd.clip()
    print(ret)
