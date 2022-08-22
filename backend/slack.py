from slack_sdk import WebClient

class Slack:
    def __init__(self, token='xoxb-3651744076246-3968426113411-sGuvyQURzhNeGXXA4auzKVv0', channel_id='C03U9T9T7C6'):
        self.channel_id = channel_id
        self.client = WebClient(token=token)
        self.users = list(list())
        self._get_users()

    def _send_msg(self, channel_id, msg):
        self.client.chat_postMessage(channel=channel_id, text=msg)

    def _send_img(self, channel_id, img_path):
        self.client.files_upload(channels=channel_id, file=img_path)

    def _reply_msg(self, channel_id, ts, msg):
        self.client.chat_postMessage(channel=channel_id, text=msg, thread_ts=ts)

    def _add_reaction(self, channel_id, names: list, ts):
        """
        names -> ['+1', '-1', 'white_check_mark']
        """
        for name in names:
            try:
                self.client.reactions_add(channel=channel_id, name=name, timestamp=ts)
            except Exception as e:
                pass

    def _get_reaction(self, channel_id, ts):
        reactions = self.client.reactions_get(channel=channel_id, timestamp=ts)['message']['reactions']
        print(reactions)

    def _get_channle_history(self, channel_id, limit=1):
        msg = self.client.conversations_history(channel=channel_id, limit=limit)['messages']
        ts = msg[0]['ts']
        return msg, ts

    def _get_replies(self, channel_id, ts, limit):
        replies = self.client.conversations_replies(channel=channel_id, ts=ts, limit=limit)['messages']
        return replies

    def _get_users(self):
        """
        user[id] -> ユーザとbotのDMのチャンネルID
        use[name] -> ユーザ名
        """
        users = self.client.users_list()['members']
        for user in users:
            is_bot = user['is_bot']
            if not is_bot:
                self.users.append((user['id'], user['name']))

    def _get_channel_users(self):
        """
        チャンネル内のユーザを取得する
        """
        users = self.client.conversations_members(channel=self.channel_id)['members']

    def _get_ims(self):
        return self.client.conversations_list(types='im')['channels']

    def check_if_emojied(self, channel_id):
        """
        指定したチャンネルのメッセージのリアクションがあるか確認する
        """
        msgs = self._get_channle_history(channel_id, 1)
        for msg in msgs:
            ts = msg['messages']['ts']
            reactions = self._get_reaction(channel_id, ts)

            for reaction in reactions:
                if reaction['name'] == 'white_check_mark':
                    continue
            for reaction in reactions:
                if reaction['name'] in ['+1', '-1']:
                    self._reply_msg(channel_id, ts, 'それはXXだよ')
                self._add_reaction(channel_id, 'white_check_mark', ts)
        return False

    def send2users(self, msg, img_path):
        """
        self.users内のユーザにbotからのDMでメッセージと画像を送る
        """
        for user_id, user_name in self.users:
            if user_name == 'slackbot':
                continue
            self._send_msg(user_id, msg)
            self._send_img(user_id, img_path)

    def send_img_msg_reaction(self, channel_id, img_path, msg):
        self._send_img(channel_id, img_path)
        self._send_msg(channel_id, msg)
        _ , ts = self._get_channle_history(channel_id)
        self._add_reaction(channel_id, ['+1', '-1'], ts)
        self._get_reaction(channel_id, ts)

    def get_latest_reply(self):
        """
        ユーザとbotのDMの最新のメッセージの中の最新のリプライを取得する
        """
        replies = list()
        for im in self._get_ims():
            id_ = im['id']
            latest_msg, ts = self._get_channle_history(id_)
            reply = self._get_replies(id_, ts, 5)
            replies.append(reply)
            self._add_reaction(id_, ['+1', '-1'], ts)
            self._get_reaction(id_, ts)

        return replies

if __name__ == '__main__':
    token = 'xoxb-3651744076246-3968426113411-sGuvyQURzhNeGXXA4auzKVv0'
    channel_id = 'C03U9T9T7C6'
    slack = Slack(token, channel_id)
    #slack.send2users('./test.jpeg')
    slack.get_latest_reply()
    slack._get_channel_users()
    slack.check_if_emojied(channel_id)
