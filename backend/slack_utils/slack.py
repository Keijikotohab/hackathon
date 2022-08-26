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

    def _send_img_msg(self, channel_id, img_path, msg):
        self.client.files_upload(channels=channel_id, file=img_path, initial_comment=msg)

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
        try:
            reactions = self.client.reactions_get(channel=channel_id, timestamp=ts)['message']['reactions']
        except:
            reactions = None
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

    def _check_has_good(self, reactions, threshold=1):
        if reactions is None:
            return False
        for reaction in reactions:
            if reaction['name'] == '+1' and reaction['count'] > threshold:
                return 'has_good'

    def _check_has_bad(self, reactions, threshold=1):
        if reactions is None:
            return False
        for reaction in reactions:
            if reaction['name'] == '-1' and reaction['count'] > threshold:
                return 'has_bad'

    def _check_has_eyes(self, reactions, threshold=0):
        if reactions is None:
            return False
        for reaction in reactions:
            if reaction['name'] == 'eyes' and reaction['count'] > threshold:
                return True
        return False

    def get_unsent_imgs(self, channel_id, limit=10):
        """
        名前を未送信のメッセージを取得して，tsと画像パスのリストを返す
        return [[ts, img_path], [ts, img_path]]
        """
        msgs, _ = self._get_channle_history(channel_id, limit)
        li = list()
        for msg in msgs:
            ts = msg['ts']
            file_name = msg['files'][0]['name'].split('.')[0]
            try:
                reactions = msg['reactions']
            except:
                pass
                # self._add_reaction(channel_id, ['white_check_mark'], ts)
                # li.append([ts, file_name])
            else:
                checked = self._check_if_checked(reactions, 'white_check_mark')
                eyed = self._check_has_eyes(reactions)
                print(checked, eyed)
                if (not checked) and eyed:
                    li.append([ts, file_name])
        print(li)
        return li

    def send_names(self, channel_id, name_list):
        """
        tsと名前のリストをもとに，名前をリプライする
        args:
            name_list: [[ts, name], [ts, name]]
        """
        for ts, name in name_list:
            msg = f'これは{name}さんです'
            self._reply_msg(channel_id, ts, msg)
            self._add_reaction(channel_id, ['white_check_mark'], ts)

    def _check_if_checked(self, reactions, mark):
        if reactions is None:
            return False
        for reaction in reactions:
            if reaction['name'] == mark:
                return True
        return False

    def check_if_emojied(self, reactions, threshold=1):
        """
        指定したチャンネルのメッセージの✅がない，かつ，👍👎があるか判定
        """
        checked = self._check_if_checked(reactions, 'white_check_mark')
        if checked:
            return False
        for reaction in reactions:
            thum_upped = reaction['name'] == '+1' and reaction['count'] > threshold
            thum_downed = reaction['name'] == '-1' and reaction['count'] > threshold
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
        self._send_img_msg(channel_id, img_path, msg)
        _, ts = self._get_channle_history(channel_id)

    def send_img_msg_reaction(self, channel_id, img_path, name, msg='この人は誰でしょう'):
        self._send_img_msg(channel_id, img_path, msg)
        _, ts = self._get_channle_history(channel_id)
        self._get_reaction(channel_id, ts)

    #def check_stamp2reply(self):
    #    """
    #    チャンネル内のメッセージにリアクションがあるかチェックする
    #    """
    #    for im in self._get_ims():
    #        print(im)
    #        id_ = im['id']
    #        msgs, ts = self._get_channle_history(id_, 10)
    #        for msg in msgs:
    #            ts = msg['ts']
    #            if ts:
    #                reply, ts = self._get_replies(id_, ts, 1)
    #                reactions = reply[0]['reactions']
    #                checked = self._check_if_checked(reactions, 'white_check_mark')
    #                #self._add_reaction(id_, ['+1', '-1'], ts)
    #                if not checked:
    #                    hand = self._check_has_hand(reactions)
    #                    if hand == 'has_good':
    #                        pass
    #                        # update?
    #                    elif hand == 'had_bad':
    #                        pass
    #                        # update?

    def get_latest_msgs(self, limit=3):

        """
        チャンネルの最新のメッセージを取得する
        """
        latest_msgs, ts = self._get_channle_history(self.channel_id, limit)
        return latest_msgs

   # def check_first_stamp(self, channel_id, msgs):
   #     """
   #     １つ目のリプライに対するスタンプをチェックする
   #     """
   #     li_good = []
   #     li_bad = []
   #     for msg in msgs:
   #         ts = msg['ts']
   #         file_name = msg['files'][0]['name'].split('.')[0]
   #         reply, _ = self._get_replies(channel_id, ts, 1)
   #         try:
   #             reply = reply[1]
   #         except:
   #             pass
   #         else:
   #             ts_reply = reply['ts']
   #             reactions = self._get_reaction(channel_id, ts_reply)
   #             if self._check_has_hand(reactions, threshold=1) == 'has_good':
   #                 li_good.append(['has_good', file_name])
   #             if self._check_has_hand(reactions, threshold=1) == 'has_bad':
   #                 li_bad.append(['has_bad', file_name])
   #     return li_good, li_bad

    def stamp2replies(self, channel_id, msgs):
        """
        msgsへの返信を全てチェックする
        グッドボタンか，バッドボタンがあるかチェックする
        return [[ts, uuid], [ts, uuid]], [[ts, uuid], [ts, uuid]]
        """
        good_list = []
        bad_list = []
        for msg in msgs:
            ts = msg['ts']
            print(ts)
            reply, _ = self._get_replies(channel_id, ts, 5)
            try:
                reply = reply[1]
            except:
                pass
            else:
                ts_reply = reply['ts']
                reactions = self._get_reaction(channel_id, ts_reply)
                if self._check_if_checked(reactions, 'white_check_mark'):
                    print('checked')
                    continue
                else:
                    self._add_reaction(channel_id, ['+1', '-1'], ts_reply) 
                    good = self._check_has_good(reactions) == 'has_good'
                    bad = self._check_has_bad(reactions) == 'has_bad'
                    if good:
                        print('good')
                        self._reply_msg(channel_id, ts, '覚えてるの！めちゃめちゃいいね')
                        self._add_reaction(channel_id, ['white_check_mark'], ts_reply)
                        good_list.append([ts, msg['files'][0]['name'].split('.')[0]])
                    elif bad:
                        print('bad')
                        self._reply_msg(channel_id, ts, 'あら，，，頑張って覚えよう')
                        self._add_reaction(channel_id, ['white_check_mark'], ts_reply)
                        bad_list.append([ts, msg['files'][0]['name'].split('.')[0]])
        return good_list, bad_list


if __name__ == '__main__':
    slack = Slack()
    li = slack.get_unsent_imgs(slack.channel_id)
    li = [[l[0], 'hori'] for l in li]
    print(li)
    slack.send_names(slack.channel_id, li)
    msgs = slack.get_latest_msgs(1)
    good, bad = slack.stamp2replies(slack.channel_id, msgs)
    print(good)
    print(bad)
