from crud import Sqlite3
from flask import Flask, render_template, request, g, jsonify, redirect, url_for
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = './static/imgs' #画像の保存場所
def allwed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in set(['png', 'jpg', 'jpeg', 'gif']) #入力を許可する形式

sql3 = Sqlite3()

@app.route("/")
def hello():
    return render_template("index.html")

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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({"id": "12345",
                            "image_path": "http://127.0.0.1/static/imgs/"+filename},
                            {"id": "67890",
                            "image_path": "http://127.0.0.1/static/imgs/"+filename},
                            {"id": "63456",
                            "image_path": "http://127.0.0.1/static/imgs/"+filename})

@app.route('/name', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        data = request.json
    print(request.json)
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
