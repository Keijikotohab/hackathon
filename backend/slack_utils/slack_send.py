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


#def job():
#    slack.give_ans(slack.channel_id)

#schedule.every(0.01).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
