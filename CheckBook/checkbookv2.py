import time, requests, json, os

url = 'https://api.ituring.com.cn/api/Search/Advanced'

data = {
    'sort': 'new',
    'page': 1,
    'isGiftBook': True
}

## headers中添加上content-type这个参数，指定为json格式
headers = {
    'Content-Type': 'application/json',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}

FILEPATH = os.getcwd() + os.sep + "books.txt"


def checkFileExist(filePath):
    return os.path.exists(filePath)


def readFile(filePath):
    booksList = []
    file = open(filePath, mode='r', encoding='utf-8')
    contents = file.readlines()
    file.close()
    for content in contents:
        booksList.append(content)
    return booksList


def updateFile(filePath, books):
    if len(books) > 0:
        file = open(filePath, mode='a+', encoding='utf-8')
        for book in books:
            file.write(book + '\n')
        file.close()


def assemblyBookInfo(name, abstract):
    name = name.strip()
    abstract = abstract.strip()
    return '[' + name + ']：' + abstract + '\n\n\n'


def notice(info):
    url = 'https://api.day.app/' + deviceId
    mess = {'title': '今天又是美好的一天！:-)', 'body': info}
    response = requests.post(url=url, headers=headers, data=json.dumps(mess)).text
    result = json.loads(response)
    if result['code'] != 200:
        print('信息发送失败！')


# 返回网页所有的书籍信息及其相应的摘要
def traverseAllBooks():
    books = []
    abstracts = []
    while True:
        response = requests.post(url=url, headers=headers, data=json.dumps(data)).text
        result = json.loads(response)
        for itor in result['bookItems']:
            books.append(itor['name'])
            abstracts.append(itor['abstract'])
        time.sleep(1)
        if result['pagination']['isLastPage']:
            break
        else:
            data['page'] += 1
    return books, abstracts


if __name__ == '__main__':
    with open('deviceId.json','r') as f:
        deviceId=json.load(f)['ID']
    booksList, abstractLists = traverseAllBooks()
    if checkFileExist(FILEPATH):
        for book in readFile(FILEPATH):
            itor = book.strip('\n')
            if itor in booksList:
                index=booksList.index(itor)
                booksList.pop(index)
                abstractLists.pop(index)
        if len(booksList) > 0:
            info=str(len(booksList))+'本新书上架\n'
            for i in range(len(booksList)):
                info+=assemblyBookInfo(booksList[i],abstractLists[i])
            notice(info)
        else:
            notice("今日无事发生")
    else:
        os.system(r"touch " + FILEPATH)
        notice("书架初始化完成")
    updateFile(FILEPATH, booksList)
