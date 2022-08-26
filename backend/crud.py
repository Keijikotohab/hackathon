import logging
import pathlib
import sqlite3

import cv2
import numpy as np

from ai.ai import FaceDetector
from slack_utils.slack import Slack

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
        dbname = "/app/db/main.db"
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
        save_path = str((pathlib.Path("static") / 'imgs' / file_name).with_suffix(".jpg"))
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

        return [{"id": id, "image_path": "http://127.0.0.1/static/imgs/"+uuid},
                {"id": id, "image_path": "http://127.0.0.1/static/imgs/"+uuid},]
        """

        clipped = self.clip(img_path)

        logger.debug('AI fin.')

        li = []

        for img, uuid in clipped:
            self.save_img(img, uuid)
            sql = f"""
            INSERT INTO main(img_path) values('{uuid}');
            """
            self.cur.execute(sql)
            li.append({"id": uuid, "image_path": "http://127.0.0.1/static/imgs/"+uuid+".jpg"})

        logger.debug('db updated')

        return li

    def fetch_all(self) -> list:
        """
        全部表示
        全部取り出し
        return: -> [(1, '47187950-5be2-41e1-b58b-2d9c13ac987b', None, 0.0, -1, 0),
                    (2, 'dc1e23fc-19c0-4bb8-acd5-38cf4615736e', None, 0.0, -1, 0)]
        """

        sql = f"""
        select * from main order by weight;
        """

        self.cur.execute(sql)
        all_date = self.cur.fetchall()
        return all_date

    def decrement_weight(self):
        sql = f"""
        UPDATE main SET weight = weight - 1 WHERE has_sent = -1;
        """
        self.cur.execute(sql)

    def fetch_unsent_zeros(self) -> list:
        # 一旦ファイル名だけ返す
        """
        return: -> [(1, '47187950-5be2-41e1-b58b-2d9c13ac987b',0.0),
                    (2, 'dc1e23fc-19c0-4bb8-acd5-38cf4615736e',0.0)]
        """

        sql = f"""
        SELECT id, img_path, weight, name FROM main WHERE (has_sent = -1) AND (weight = 0);
        """
        self.cur.execute(sql)
        unsent_zeros = self.cur.fetchall()
        return unsent_zeros

    def change_has_sent(self, condition: str):
        """
        condition -> ex. WHERE decay = 0
        """

        sql = f"""
        UPDATE main SET has_sent = -1 * has_sent {condition};
        """
        self.cur.execute(sql)

    def fetch_step(self, id_) -> int:
        """
        return: -> int
        """
        sql = f"""
        SELECT step FROM main WHERE id = {id_};
        """
        self.cur.execute(sql)
        return self.cur.fetchone()[0]

    def update_field(self, id_, field_name: str, value: any):
        """
        field_name -> ex. weight, step
        value -> ex. 1.0, 2
        """
        sql = f"""
        UPDATE main SET {field_name} = {value} WHERE id = {id_};
        """
        self.cur.execute(sql)

    def set_name(self, img_path, value: str):
        self.cur.execute("UPDATE main SET name = ? WHERE img_path = ?", (value, img_path))
        self.cur.execute("UPDATE main SET weight = ? WHERE img_path = ?", (3, img_path))
    
    def set_has_sent(self, img_path):
        self.cur.execute("UPDATE main SET has_sent = ? WHERE img_path = ?", (1, img_path))

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
