from slack_sdk import WebClient

class Slack:
    def __init__(self, token='xoxb-3651744076246-3968426113411-sGuvyQURzhNeGXXA4auzKVv0', channel_id='C03U9T9T7C6'):
        self.channel_id = channel_id
        self.client = WebClient(token=token)

    def send_msg(self, msg):
        self.client.chat_postMessage(channel=self.channel_id, text=msg)
        return True

    def send_img(self, img):
        self.client.files_upload(channels=self.channel_id, file=img)
        return True

if __name__ == '__main__':
    token = 'xoxb-3651744076246-3968426113411-sGuvyQURzhNeGXXA4auzKVv0'
    channel_id = 'C03U9T9T7C6'
    slack = Slack(token, channel_id)
    slack.send_msg('Hello World')
    slack.send_img('./test.jpeg')
