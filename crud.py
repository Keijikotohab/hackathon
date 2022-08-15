import sqlite3
from uuid import uuid4

# とりあえず仮のクラス
class AI:
    def __init__(self, img):
        pass

    def clip(self):
        return {'aa-aa-bb': "img1", 'bb-bb-cc': "img2", 'cc-cc-dd': "img3"}

# とりあえず仮のクラス
class Index:
    def __init__(self):
        pass

    def get_name(self):
        return {'aa-aa-bb': "Ito", 'bb-bb-cc': "Kojima", 'cc-cc-dd': "Kamiya"}

    def new_weight(self):
        return {'aa-aa-bb': 1, 'bb-bb-cc': 2, 'cc-cc-dd': 3}


class Sqlite3:
    def __init__(self):
        dbname = "main.db"
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def create(self, img=None):
        imgs = AI(img).clip()

        # ここでindex.htmlにもわたす
        # img_path兼uuidで識別する

        for img_path, _ in imgs.items():
            sql = f"""
            INSERT INTO main(img_path) values('{img_path}');
            """
            self.cur.execute(sql)

    def read(self):
        sql = f"""
        select * from main;
        """
        self.cur.execute(sql)
        print(self.cur.fetchall())

    def update_name(self):
        index = Index().new_weight()
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

if __name__ == '__main__':
    sq = Sqlite3()
    sq.delete_all_items()

    sq.create()
    sq.read()

    sq.update_name()
    sq.read()

    sq.update_weight()
    sq.read()

    sq.close()
