import logging
from slack import Slack
import pathlib
import sqlite3

import cv2
import numpy as np

from ai import FaceDetector

logger = logging.getLogger("mylog")
logger.setLevel(logging.DEBUG)

# とりあえず仮のクラス
class Index:
    def __init__(self):
        pass

    def get_name(self):
        return {"aa-aa-bb": "Ito", "bb-bb-cc": "Kojima", "cc-cc-dd": "Kamiya"}

    def new_weight(self):
        return {"aa-aa-bb": 1, "bb-bb-cc": 2, "cc-cc-dd": 3}


class Sqlite3:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        dbname = "main.db"
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def save_img(self, img: np.ndarray, file_name: str, save_dir: str = "img"):
        """
        ローカルのimgフォルダに保存
        """

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        save_path = str((pathlib.Path("static") / 'imgs'/ file_name).with_suffix(".jpg"))
        print(save_path)
        cv2.imwrite(save_path, img)

    def clip(self, img_path: str) -> list:
        """
        画像を切り取る
        """

        fd = FaceDetector(img_path)
        fd.predict()
        clipped = fd.clip()
        return clipped

    def create(self, img_path: str = "test.jpeg"):
        """
        切り取った画像をフォルダに保存
        切り取った画像のデータをDBに保存
        """

        clipped = self.clip(img_path)

        li = []

        for img, uuid in clipped:
            self.save_img(img, uuid)
            sql = f"""
            INSERT INTO main(img_path) values('{uuid}');
            """
            self.cur.execute(sql)
            li.append({"id": uuid, "image_path": "http://127.0.0.1/static/imgs/"+uuid})

        logger.debug('created')

        return li

    def read(self) -> list:
        """
        全部表示
        全部取り出し
        """

        sql = f"""
        select * from main order by weight;
        """

        self.cur.execute(sql)
        all_date = self.cur.fetchall()
        return all_date

    def update_name(self, index):
        for img_path, weight in index.items():
            sql = f"""
            UPDATE main set weight = {weight} where img_path = '{img_path}';
            """
            self.cur.execute(sql)

    def update_weight(self):
        index = Index().get_name()
        for img_path, name in index.items():
            sql = f"""
            UPDATE main set name = '{name}' where img_path = '{img_path}';
            """
            self.cur.execute(sql)

    # 今回は最悪作らない
    def delete_all_items(self):
        sql = f"""
        DELETE FROM main;
        """
        self.cur.execute(sql)
        self.conn.commit()


if __name__ == "__main__":
    slack = Slack()
    sq = Sqlite3()
    sq.connect()

    sq.delete_all_items()

    imgs = sq.create()
    print(imgs)
    for img in imgs:
        file_path = './static/imgs/' + img['id'] + '.jpg'
        print(file_path)
        slack.send_img(file_path)

    sq.read()

    index = Index().new_weight()
    sq.update_name(index)
    sq.read()

    sq.update_weight()
    sq.read()

    sq.close()
