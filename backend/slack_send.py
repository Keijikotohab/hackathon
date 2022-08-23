import datetime
import time
import schedule
from slack import Slack
from crud import Sqlite3
slack = Slack()
sql = Sqlite3()
sql.connect()

def job():
    slack.give_ans(slack.channel_id)

def recommend():
    #sql.connect()
    print(datetime.datetime.now())
    #【15分に1回の更新部分】
    #sql.decrement_weight()#送っていないものの時間を更新

    #【残り0分だった要素の抽出】
    print(sql.fetch_unsent_zeros())
    """
  {
        id:"sdf",
        img_path:"~.jpeg"
    },
    {
        id:"sdf",
        img_path:"~.jpeg"
    }
    """

    #【残り0分だった要素の送信】

    id_ = slack.channel_id # 本来はDBから取得する
    img_path = "static/imgs/"+request.json[i]["id"]+".jpg"
    msg = request.json[i]["name"]+"さんが登録されました。皆さん名前を覚えましょう。"
    slack.send_img_msg_reaction(id_, img_path, msg)
    
    #【送信した要素の更新】
    
    sql.change_has_sent("has_sentに変更")
    #sql.fetch_unsent_zeros()
    
schedule.every(0.01).minutes.do(job)
schedule.every(0.01).minutes.do(recommend)#15分ごと

while True:
    schedule.run_pending()
    time.sleep(1)
