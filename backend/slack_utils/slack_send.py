import datetime
import os
import time

import schedule
from dotenv import load_dotenv
from slack import Slack

from crud import Sqlite3

load_dotenv()
slack_token = os.getenv("SLACK_TOKEN")
slack_channel_id = os.getenv("SLACK_CHANNEL_ID")

slack = Slack()
sql = Sqlite3()
sql.connect()


def job():
    slack.give_ans(slack.channel_id)

def recommend():
    sql.connect()
    sql.decrement_weight()
    sql.close()


    sql.connect()
    print(sql.fetch_unsent_zeros())
    unsent_list = sql.fetch_unsent_zeros()
    for i in range(len(unsent_list)):
        slack.send_img_msg_reaction(slack.channel_id,"static/imgs/"+unsent_list[i][1]+".jpg", "この人は誰でしょう？")
        sql.set_has_sent(unsent_list[i][1])
    for i in range(len(unsent_list)):
        print("名前"+unsent_list[i][1])
    sql.close()

    print("実行")

    # 【15分に1回の更新部分】
    #sql.decrement_weight()#

    # 【残り0分だった要素の抽出】
    #print(sql.fetch_unsent_zeros())


schedule.every(0.05).minutes.do(job)
schedule.every(0.1).minutes.do(recommend)

while True:
    schedule.run_pending()
    time.sleep(1)
