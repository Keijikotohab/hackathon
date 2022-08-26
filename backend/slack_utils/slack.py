import os

from dotenv import load_dotenv
from slack_sdk import WebClient

# .envファイルの内容を読み込見込む
load_dotenv()


class Slack:
    def __init__(self, token=os.environ['SLACK_TOKEN'], channel_id='C03U9T9T7C6'):
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
        return reactions

    def _get_channle_history(self, channel_id, limit=1):
        msg = self.client.conversations_history(channel=channel_id, limit=limit)['messages']
        try:
            ts = msg[0]['ts']
        except:
            ts = None
        return msg, ts

    def _get_replies(self, channel_id, ts, limit):
        replies = self.client.conversations_replies(channel=channel_id, ts=ts, limit=limit)['messages']
        try:
            ts = msg[0]['ts']
        except:
            ts = None
        return replies, ts

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

    def give_ans(self, channel_id, limit=10):
        msgs, _ = self._get_channle_history(channel_id, limit)
        for msg in msgs:
            ts = msg['ts']
            try:
                reactions = msg['reactions']
                print("リアクション",reactions)
            except:
                pass
            else:
                if self.check_if_emojied(reactions):
                    self._reply_msg(channel_id, ts, 'この人は〇〇です！知っていましたか？知っている人は👍、知らない人は👎をお願いします。')
                    self._add_reaction(channel_id, ['white_check_mark'], ts)

    def check_if_emojied(self, reactions):
        """
        指定したチャンネルのメッセージの✅がない，かつ，👍👎があるか判定
        """
        for reaction in reactions:
            if reaction['name'] == 'white_check_mark':
                return False
        for reaction in reactions:
            thum_upped = reaction['name'] == '+1' and reaction['count'] > 1
            thum_downed = reaction['name'] == '-1' and reaction['count'] > 1
            if thum_upped or thum_downed:
                return True

    def send2users(self, msg, img_path):
        """
        self.users内のユーザにbotからのDMでメッセージと画像を送る
        """
        for user_id, user_name in self.users:
            if user_name == 'slackbot':
                continue
            self._send_msg(user_id, msg)
            self._send_img(user_id, img_path)

    def send_img_msg(self, channel_id, img_path, msg):
        self._send_img(channel_id, img_path)
        self._send_msg(channel_id, msg)
        _, ts = self._get_channle_history(channel_id)

    def send_img_msg_reaction(self, channel_id, img_path, msg):
        self._send_img(channel_id, img_path)
        self._send_msg(channel_id, msg)
        _, ts = self._get_channle_history(channel_id)
        self._add_reaction(channel_id, ['+1'], ts)
        self._get_reaction(channel_id, ts)

    def check_stamp2reply(self):
        """
        チャンネル内のメッセージにリアクションがあるかチェックする
        """
        for im in self._get_ims():
            print(im)
            id_ = im['id']
            msgs, ts = self._get_channle_history(id_)
            if ts:
                reply, ts = self._get_replies(id_, ts, 1)
                reaction = self._get_reaction(id_, ts)


    def get_latest_reply(self):
        """
        ユーザとbotのDMの最新のメッセージの中の最新のリプライを取得する
        """
        replies = list()
        for im in self._get_ims():
            id_ = im['id']
            latest_msg, ts = self._get_channle_history(id_)
            if ts:
                reply, _ = self._get_replies(id_, ts, 5)
                replies.append(reply)
                self._add_reaction(id_, ['+1', '-1'], ts)
                self._get_reaction(id_, ts)

        return replies

if __name__ == '__main__':
    slack = Slack()
    slack.get_latest_reply()
    slack.check_stamp2reply()
