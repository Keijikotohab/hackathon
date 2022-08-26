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
    sql.connect()
    send_name_list = []
    li = slack.get_unsent_imgs(slack.channel_id)
    for i in range(len(li)):
        send_name_list.append([li[i][0],sql.change_path_to_name(li[i][1])])
    print(send_name_list)
    slack.send_names(slack.channel_id, send_name_list)

    msg_list = slack.get_latest_msgs()
    good, bad = slack.stamp2replies(slack.channel_id,msg_list)
    for i in range(len(good)):
        next_send_time = sql.update_weight(good[i][1],True)
        sql.set_has_not_sent(good[i][1])
        slack._reply_msg(slack.channel_id,good[i][0],'覚えてきましたね！次は'+str(next_send_time)+'分後に通知します!')


    for i in range(len(bad)):
        next_send_time = sql.update_weight(bad[i][1],False)
        sql.set_has_not_sent(bad[i][1])
        slack._reply_msg(slack.channel_id,bad[i][0],'残念でした！次は'+str(next_send_time)+'分後に通知します!')



    sql.close()



def recommend():
    sql.connect()
    sql.decrement_weight()
    sql.close()


    sql.connect()
    print(sql.fetch_unsent_zeros())
    unsent_list = sql.fetch_unsent_zeros()
    for i in range(len(unsent_list)):
        slack.send_img_msg_reaction(slack.channel_id,"static/imgs/"+unsent_list[i][1]+".jpg", unsent_list[i][3])
        sql.set_has_sent(unsent_list[i][1])
    for i in range(len(unsent_list)):
        print("名前"+unsent_list[i][3])
    sql.close()

    print("実行")

    # 【15分に1回の更新部分】
    #sql.decrement_weight()#

    # 【残り0分だった要素の抽出】
    #print(sql.fetch_unsent_zeros())


schedule.every(0.01).minutes.do(job)
schedule.every(0.1).minutes.do(recommend)

while True:
    schedule.run_pending()
    time.sleep(1)
