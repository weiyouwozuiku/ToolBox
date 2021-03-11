# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 9:11
# @Author  : buer
# @Email   : weiyouwozuiku@gmail.com

import smtplib,traceback,os,requests,urllib,json
from email.mime.text import MIMEText
from email.header import Header

version='UnicomTask'

#返回要推送的通知内容
#对markdown的适配要更好
#增加文件关闭操作
def readFile(filepath):
    content = ''
    with open(filepath, encoding='utf-8') as f:
        for line in f.readlines():
            content += line 
    return content

#返回要推送的通知内容
#对text的适配要更好
#增加文件关闭操作
def readFile_text(filepath):
    content = ''
    with open(filepath, encoding='utf-8') as f:
        for line in f.readlines():
            content += line
    return content

#返回要推送的通知内容
#对html的适配要更好
#增加文件关闭操作
def readFile_html(filepath):
    content = ''
    with open(filepath, "r" , encoding='utf-8') as f:
        for line in f.readlines():
            content += line + '<br>'
    return content

#自己的邮件推送
def sendEmail(receiveAddress):
    try:
        #要发送邮件内容
        content = readFile(os.getcwd()+os.sep+version+os.sep+'log.txt')
        #邮件
        info=MIMEText(content,'plain','utf-8')
        info['Subject']=Header('UnicomTask每日报表','utf-8')
        #设定发送的邮箱
        sendAddress = ''
        info['From']=Header(sendAddress)
        info['To']=Header(receiveAddress)
        #设置自己的邮箱授权码
        password=''
        #设置自己的邮箱smtp地址
        smtpServer=''
        server=smtplib.SMTP_SSL(smtpServer,465)
        flag=server.login(sendAddress,password)
        server.sendmail(sendAddress,[receiveAddress],info.as_string())
        server.quit()
        print('邮件发送成功')
    except Exception as e:
        print('邮件推送异常，原因为: ' + str(e))
        print(traceback.format_exc())
    
    

#钉钉群自定义机器人推送
def sendDing(webhook):
    try:
        #要发送邮件内容
        content = readFile(os.getcwd()+os.sep+version+os.sep+'log.txt')
        data = {
            'msgtype': 'markdown',
            'markdown': {
                'title': 'UnicomTask每日报表',
                'text': content
            }
        }
        headers = {
            'Content-Type': 'application/json;charset=utf-8'
        }
        res = requests.post(webhook,headers=headers,json=data)
        res.encoding = 'utf-8'
        res = res.json()
        print('dinngTalk push : ' + res['errmsg'])
    except Exception as e:
        print('钉钉机器人推送异常，原因为: ' + str(e))
        print(traceback.format_exc())

#发送Tg通知
def sendTg(tgBot):
    try:
        token = tgBot['tgToken']
        chat_id = tgBot['tgUserId']
        #发送内容
        content = readFile_text(os.getcwd()+os.sep+version+os.sep+'log.txt')
        data = {
            'UnicomTask每日报表':content
        }
        content = urllib.parse.urlencode(data)
        #TG_BOT的token
        #token = os.environ.get('TG_TOKEN')
        #用户的ID
        #chat_id = os.environ.get('TG_USERID')
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={content}'
        session = requests.Session()
        resp = session.post(url)
        print(resp)
    except Exception as e:
        print('Tg通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())

#发送push+通知
def sendPushplus(token):
    try:
        #发送内容
        data = {
            "token": token,
            "title": "UnicomTask每日报表",
            "content": readFile_html(os.getcwd()+os.sep+version+os.sep+'log.txt')
        }
        url = 'http://pushplus.hxtrip.com/send/'
        headers = {'Content-Type': 'application/json'}
        body = json.dumps(data).encode(encoding='utf-8')
        resp = requests.post(url, data=body, headers=headers)
        print(resp)
    except Exception as e:
        print('push+通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())

#企业微信通知，普通微信可接收
def sendWechat(wex):
    #获得access_token
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    token_param = '?corpid=' + wex['id'] + '&corpsecret=' + wex['secret']
    token_data = requests.get(url + token_param)
    token_data.encoding = 'utf-8'
    token_data = token_data.json()
    access_token = token_data['access_token']
    #发送内容
    content = readFile_text(os.getcwd()+os.sep+version+os.sep+'log.txt')
    #创建要发送的消息
    data = {
        "touser": "@all",
        "msgtype": "text",
        "agentid": wex['agentld'],
        "text": {"content": content}
    }
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    message = requests.post(send_url,json=data)
    message.encoding = 'utf-8'
    res = message.json()
    print('Wechat send : ' + res['errmsg'])
