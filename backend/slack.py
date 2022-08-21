from slack_sdk import WebClient

class Slack:
    def __init__(self, token='xoxb-3651744076246-3968426113411-sGuvyQURzhNeGXXA4auzKVv0', channel_id='C03U9T9T7C6'):
        self.channel_id = channel_id
        self.client = WebClient(token=token)
        self.users = list(list())
        self.replies = list()

    def _send_msg(self, id_, msg):
        self.client.chat_postMessage(channel=id_, text=msg)

    def _send_img(self, id_, img_path):
        self.client.files_upload(channels=id_, file=img_path)

    def get_users(self):
        users = self.client.users_list()['members']
        for user in users:
            print(user)
            is_bot = user['is_bot']
            if not is_bot:
                self.users.append((user['id'], user['name']))

    def send2users(self, img_path):
        for user_id, user_name in self.users:
            print(user_id, user_name)
            if user_name == 'slackbot':
                continue
            self._send_msg(user_id, 'Hello ' + user_name)
            self._send_img(user_id, img_path)

    def _get_ims(self):
        return self.client.conversations_list(types='im')['channels']
        
    def get_latest_reply(self):
        for im in self._get_ims():
            id_ = im['id']
            latest_message = self.client.conversations_history(channel=id_, limit=1)['messages']
            ts = latest_message[0]['ts']
            reply = self.client.conversations_replies(channel=id_, ts=ts, limit=5)['messages'][-1]['text']
            self.replies.append(reply)

if __name__ == '__main__':
    token = 'xoxb-3651744076246-3968426113411-sGuvyQURzhNeGXXA4auzKVv0'
    channel_id = 'C03U9T9T7C6'
    slack = Slack(token, channel_id)
    slack.get_users()
    #slack.send2users('./test.jpeg')
    slack.get_latest_reply()
