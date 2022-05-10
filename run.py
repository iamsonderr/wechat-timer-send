import requests
import json
import time
from wxpy import *

def get_sweet():
    """获取随机彩虹屁"""
    # 1. 随机彩虹屁获取接口 URL
    #url = "https://api.muxiaoguo.cn/api/dujitang?api_key=9a9814e933f3cac8"
    url = "https://api.muxiaoguo.cn/api/caihongpi?api_key=6eb006847f76e3fd"
    # 2. 获取返回数据
    sweet_data = requests.get(url)
    # 3. 解析数据为json格式并返回
    sweet_data_json = sweet_data.json()	
    sweet_sentence = sweet_data_json['data']['comment']
    return sweet_sentence

def send_news(my_friend, sentence):
    try:
        my_friend.send(sentence)
    except:
        my_friend.send(u"今天消息发送失败了")
if __name__ == '__main__':
    #print(get_sweet())
    bot = Bot()
    my_friend = bot.friends().search("一个半柠檬C")[0] #注意这个[0]
    #print(my_friend)
    send_news(my_friend,"（狂喝毒鸡汤开启模式）!!!")
    i = 1
    while True:
        send_news(my_friend,get_sweet()+"\n\n"+"[第"+"{}".format(i)+"条毒鸡汤]")
        i = i + 1
        # 这里设置间隔时间，单位为秒
        time.sleep(1)
