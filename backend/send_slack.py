from slack_main import slack
from crud import Sqlite3

slack = Slack(token, channel_id)
sq = Sqlite3()
img_path = sq.get_img_to_send()
slack.send2users(img_path)
