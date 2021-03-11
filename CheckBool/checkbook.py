# -*- coding: utf-8 -*-
import requests,smtplib
from lxml import html
from email.mime.text import MIMEText
from email.header import Header
from bs4 import BeautifulSoup
import os

URL="https://www.ituring.com.cn/book?tab=gift"
BASEURL="https://www.ituring.com.cn/book?tab=gift&sort=new&page="
FAKEHEADER={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}
FILEPATH=os.getcwd()+os.sep+"books.txt"

def getPageNumber(url):
    # 可兑换样书首页
    page=requests.get(url,headers=FAKEHEADER)
    pageTree=html.fromstring(page.text)
    pageNumber=pageTree.xpath('//*[@id="tab-book"]/div[1]/div[3]/div/ul/li[7]/a')[0].text
    return pageNumber

def createAllPage(pageNumber):
    # 拼接网页
    pageList=[]
    for itor in range(0, int(pageNumber)):
        pageList.append(BASEURL+str(itor))
    return pageList

def traverseAllPage(pageList):
    books=[]
    # 遍历所有网页
    for page in pageList:
        bs=BeautifulSoup(requests.get(page).content,"lxml")
        for name in bs.select('.name'):
            bookName=name.contents[0].contents[0]
            books.append(bookName)
    return books

def checkFileExist(filePath):
    if os.path.exists(filePath):
        return True
    else:
        return False

def readFile(filePath):
    booksList=[]
    file=open(filePath,mode='r',encoding='utf-8')
    contents=file.readlines()
    file.close()
    for content in contents:
        booksList.append(content)
    return booksList

def updateFile(filePath,books):
    if len(books)>0:
        file = open(filePath, mode='w',encoding='utf-8')
        for book in books:
            file.write(book + '\n')
        file.close()

def sendEmail(msg,books=None):
    message=""
    if books:
        message+="今天又是美好的一天！:-)\n以下是今日新上架书籍名称：\n"
        for book in books:
            message+=book+'\n'
    else:
        message="今天又是美好的一天！\n但是没有新书上架！:-("
    #邮件正文
    info=MIMEText(message,'plain','utf-8')
    #邮件主题
    info['Subject']=Header(msg,'utf-8')
    #发信人
    sendAddress = ''
    info['From']=Header(sendAddress)
    #收件人
    receiveAddress=''
    info['To']=Header(receiveAddress)
    #授权码
    password=''
    smtpServer='smtp.163.com'
    try:
        #因为腾讯云和阿里云将25端口封了，在此使用465端口
        server=smtplib.SMTP_SSL(smtpServer,465)
        flag=server.login(sendAddress,password)
        server.sendmail(sendAddress,[receiveAddress],info.as_string())
        server.quit()
    except smtplib.SMTPException as e:
        print("邮件发送失败"+str(e))


if __name__ == '__main__':
    pageNumber=getPageNumber(URL)
    pageList=createAllPage(pageNumber)
    #现在可以兑换的所有书籍
    books = traverseAllPage(pageList)
    if checkFileExist(FILEPATH):
        #可以兑换或曾可以兑换书籍
        booksList=readFile(FILEPATH)
        for book in booksList:
            itor=book.strip('\n')
            if itor in books:
                books.remove(itor)
        if len(books)>0:
            sendEmail(str(len(books))+"本新书上架",books)
        else:
            sendEmail("今日无事发生")
    else:
        os.system(r"touch "+FILEPATH)
        sendEmail("书架初始化完成")
    updateFile(FILEPATH, books)
