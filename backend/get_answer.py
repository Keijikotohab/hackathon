from skack import Slack

token = 'xoxb-3651744076246-3968426113411-sGuvyQURzhNeGXXA4auzKVv0'
channel_id = 'C03U9T9T7C6'

slack = Slack(token, channel_id)

reply_list = slack.get_lateest_reply()

"""
some 集計プロセス
"""

sql3.update_weight()
