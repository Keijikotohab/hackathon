from flask import Flask, render_template
from crud import Splite3

app = Flask(__name__)
sql3 = Sqlite3()

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/split_img")
def hello():
    ```
    画像のパスをJSから受け取ってcrudに投げる
    crudは，切り取り済み画像をフォルダに保存してそのパスをDBに保存
    ```
    img_path = 'test.jpeg'
    sql3.create(img_path)
    return render_template("index.html")

@app.route("/register")
def hello():
    ```
    DBの名前をアップデート
    ```
    # JSからの諸々
    name_dict = {"aa-aa-bb": "Ito", "bb-bb-cc": "Kojima", "cc-cc-dd": "Kamiya"}
    sql3.update_name(name_dict)

    return render_template("index.html")

@app.route("/index")
def hello():
    ```
    登録一覧を確認する
    ```
    # 結構未実装かも
    sql3.read()

    return render_template("index.html")


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
