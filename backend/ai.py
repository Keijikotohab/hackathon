import logging
import cv2
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

    # Re-Develop ME
    def clip(self) -> list:
        """
        bboxの情報をもとに，写真を切り抜く。
        return [切り抜いた写真, uuid, bbox]
        """
        li = list()
        for uuid, bbox in self.bboxes:
            topleft_x, topleft_y, bottomright_x, bottomright_y = bbox
            topleft_x, topleft_y, bottomright_x, bottomright = int(0.9 * topleft_x), int(0.9 * topleft_y), int(1.1 * bottomright_x), int(1.1 * bottomright_y)
            img = self.orgimg[topleft_y:bottomright_y, topleft_x:bottomright_x]
            li.append([img, uuid])

        return li


if __name__ == "__main__":
    print('start')
    fd = FaceDetector("test.jpeg")
    fd.predict()
    ret = fd.clip()
