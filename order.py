import requests
import json


# def ai_talk(question):
#     return question.replace('你', '我').replace('不', '').replace('吗', '').replace('?', '!').replace('？', '！')

# 天气查询
def tianqi():
    city = input('请输入需要查询的城市:')
    url = 'https://tianqiapi.com/api?version=v61&appid=11695963&appsecret=zf3for6A&city='+city+''
    res = requests.get(url)
    tq_text = res.text
    tq_json=json.loads(tq_text)
    wendu = tq_json['tem']
    gw = tq_json['tem1']
    dw = tq_json['tem2']
    tq = tq_json['wea']
    print(f'{city}:温度:{wendu}℃,天气:{tq},高温:{gw}℃,低温:{dw}℃')

# 词语查询
def ciyu():
    ciyu=input('请输入查询词语:')
    url = 'http://api.avatardata.cn/CiHai/LookUp?key=d532112ef6f640509283371629639e1d&keyword='+ciyu+''
    res = requests.get(url)
    cy_text = res.text
    cy_json=json.loads(cy_text)
    cy=cy_json['result']['words']
    ys=cy_json['result']['content']
    right = ys[ys.find('b') + 3:]
    result = right[:right.find('ys')]
    print(cy,f'意思：{result}')

# 历史上的今天
def ls():
    yue = input('请输入月份:')
    ri = input('请输入日期:')
    url = ' http://api.avatardata.cn/HistoryToday/LookUp?key=75660e183203492c9646fc675dacff35&yue=' + yue + '&ri=' + ri + '&type=1&page=1&rows=5'
    res = requests.get(url)
    ls_text = res.text
    ls_json = json.loads(ls_text)
    yi = ls_json['result'][0]['year']
    yi_1 = ls_json['result'][0]['title']
    er = ls_json['result'][1]['year']
    er_1 = ls_json['result'][1]['title']
    san = ls_json['result'][2]['year']
    san_1 = ls_json['result'][2]['title']
    si = ls_json['result'][3]['year']
    si_1 = ls_json['result'][3]['title']
    wu = ls_json['result'][4]['year']
    wu_1 = ls_json['result'][4]['title']
    print('历史上的今天:')
    print(
        f'{yi}年,{yue}月{ri}日,事件:{yi_1}\n{er}年,{yue}月{ri}日,事件:{er_1}\n{san}年,{yue}月{ri}日,事件:{san_1}\n{si}年,{yue}月{ri}日,事件:{si_1}\n{wu}年,{yue}月{ri}日,事件:{wu_1}')

# ip查询
def ip():
    ip = input('请输入ip地址:')
    url = ' http://api.avatardata.cn/IpLookUp/LookUp?key=c1275b68faf5415fbeecaa486aa61e41&ip='+ip+''
    res = requests.get(url)
    ip_text = res.text
    ip_json = json.loads(ip_text)
    dd = ip_json['result']['area']
    ly = ip_json['result']['location']
    if ly=='':
        print(f'地点:{dd},来源:未知')
    else:
        print(f'地点:{dd},来源:{ly}')