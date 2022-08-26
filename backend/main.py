import os

from crud import Sqlite3
from flask import (Flask, g, jsonify, redirect, render_template, request,
                   url_for)
from flask_cors import CORS
from werkzeug.utils import secure_filename

from slack_utils.slack import Slack

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = './static/imgs' #画像の保存場所
def allwed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in set(['png', 'jpg', 'jpeg', 'gif']) #入力を許可する形式

sql3 = Sqlite3()
slack = Slack()

@app.route('/images', methods=['GET', 'POST'])
def uploads_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
        if file and allwed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)

            sql3.connect()
            print('before')
            clipped_imgs = sql3.create(save_path)
            print('after')
            sql3.close()
            print('clipped imgs:')
            print(clipped_imgs)

            return jsonify(clipped_imgs)
            """
            return jsonify([{"id": "12345",
                            "image_path": "http://127.0.0.1/static/imgs/"+filename},
                            {"id": "67890",
                            "image_path": "http://127.0.0.1/static/imgs/"+filename},
                            {"id": "63456",
                            "image_path": "http://127.0.0.1/static/imgs/"+filename}])
            """

@app.route('/name', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        data = request.json
    print(len(request.json))
    print(request.json[0]["name"])
    print(request.json[1]["name"])

    for i in range(len(request.json)):
        id_ = slack.channel_id
        img_path = "static/imgs/"+request.json[i]["id"]+".jpg"
        msg = request.json[i]["name"]+"さんが登録されました。皆さん名前を覚えましょう。"
        sql3.connect()
        sql3.set_name(request.json[i]["id"], request.json[i]["name"])
        sql3.close()
        slack.send_img_msg(id_, img_path, msg)
    return ""

@app.route("/split_img")
def split_img():
    """
    画像のパスをJSから受け取ってcrudに投げる
    crudは，切り取り済み画像をフォルダに保存してそのパスをDBに保存
    """
    img_path = 'test.jpeg'
    sql3.create(img_path)
    return render_template("index.html")

@app.route("/register")
def register():
    """
    DBの名前をアップデート
    """
    # JSからの諸々
    name_dict = {"aa-aa-bb": "Ito", "bb-bb-cc": "Kojima", "cc-cc-dd": "Kamiya"}
    sql3.update_name(name_dict)

    return render_template("index.html")

@app.route("/update_weight")
def update_weight():
    """
    DBのweightをアップデート
    """
    # JSからの諸々
    weight_dict = {"aa-aa-bb": "60", "bb-bb-cc": "70", "cc-cc-dd": "80"}
    sql3.update_weight(weight_dict)

    return render_template("index.html")

@app.route("/index")
def index():
    """
    登録一覧を確認する
    """
    # 結構未実装かも
    sql3.read()

    return render_template("index.html")


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
