from crud import Sqlite3

imgs = Sqlite3().read()
# 小島さんが作ってる
slack = Slack(token, channel_name)

for img in imgs:
    print('img')
    print(img)
    slack.send_img(img)
