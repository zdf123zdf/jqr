import time
from datetime import datetime
import order
import guess
import calendar
import urllib
import requests

print('----------------------')
print('欢迎使用咸鱼机器人0.5版本')
print('----------------------')

print('''
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]咸鱼[-]''')
print('-----------------------')

# 初始时间
def sj():
    localTime = time.localtime(time.time())
    localTimeStrs = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
    print('现在时间是：', localTimeStrs)
sj()

time.sleep(1)

name = input('我是咸鱼，请问怎么称呼？')
# 功能介绍
def hello():
    print('你好，' + name + '，我是你的咸鱼机器人！')
    print('您可以输入：')
    print('时间---------查询时间与日历\n每日一言--------名人名句\n年龄—---------查询年龄\n天气----------查询城市天气\n猜数字--------小游戏猜数字\n猜拳----------石头剪刀布游戏\n辞海----------词语查询\n历史上的今天---查看历史上的今天\nip查询--------查看ip地址来源\n88-----------退出机器人')
hello()

# 功能项目
def xm():
    print('-----------------------')
    print('您有什么吩咐？')
    cmd = input('>>>')

# 每日一言
    if cmd == '一言':
        def lzs():
            url = ('http://zdfyy.aote.xyz/yan/api.php')
            res = requests.get(url)
            y_text = res.text
            print(y_text)
        lzs()
        xm()

# 年龄
    elif cmd == "年龄":
        def age():
            age = int(input('请告诉我你的年龄：'))
            if (age <= 12):
                print(f"{age}岁还是个小屁孩呢！")
            elif (age > 12 and age <= 30):
                print(f"{age}岁，真令人羡慕！")
            elif (age > 30 and age <= 60):
                print("您一定有丰富的人生阅历")
            else:
                print('你在家中肯定是个宝')
        age()
        xm()

# 获取时间与日历
    elif cmd == "时间":
        print('您可以输入：\n几点了？-------查看当前时间\n日历----------输入年份与月份查看日历')
        def time():
            a = input('>>>')
            dt = datetime.now()
            if a == '几点了？':
                print(dt.strftime('今天是:%Y年%m月%d日 现在是:%H:%M:%S'))
            elif a == '日历':
                nian = int(input('请输入年份:'))
                yue = int(input('请输入月份:'))
                cal = calendar.month(nian, yue)
                print(cal)
        time()
        xm()

# 闰年判断
    elif cmd == "闰年判断":
        def t():
            t=int(input('请输入年份:'))
            if t/400==int(t/400):
                print(f'{t}年是闰年')
            elif (t / 4 == int(t / 4)) and (t / 100 != int(t / 100)):
                print(f'{t}年是闰年')
            else:
                print(f"{t}年不是闰年")
        t()
        xm()

# 结束
    elif cmd == "88":
        print('88，有需要再找我！')
        return

# 天气预报
    elif cmd == "天气":
            order.tianqi()
            xm()

# 猜数字游戏
    elif cmd == '猜数字':
       guess.csz()
       xm()

# 辞海
    elif cmd == '词语':
        order.ciyu()
        xm()

# 历史上的今天
    elif cmd == '历史上的今天':
        order.ls()
        xm()

# ip查询
    elif cmd == 'ip' and 'ip查询':
        order.ip()
        xm()

# 猜拳
    elif cmd == '猜拳':
        guess.cq()
        xm()

    else:
        def qingyunke(cmd):
            url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(cmd))
            html = requests.get(url)
            return html.json()["content"]
        res = qingyunke(cmd)
        print(res)
        xm()
xm()
