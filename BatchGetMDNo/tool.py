def saveToMD(msg):
    try:
        with open("demo.md", 'a+') as f:
            f.write(msg+"\n\n")
            f.close()
    except Exception as e:
        if 'f' in dir():
            f.close()


index = int(input("please input the index:"))
pre100 = 1
pre500 = 1
pre1000 = 1
for i in range(1, index):
    if i % 1000 == 1:
        saveToMD("## " + str(pre1000) + '~' + str(pre1000 + 1000 - 1))
        pre1000 += 1000
    if i % 500 == 1:
        saveToMD("### " + str(pre500) + '~' + str(pre500 + 500 - 1))
        pre500 += 500
    if i % 100 == 1:
        saveToMD("#### "+str(pre100)+'~'+str(pre100 + 100 - 1))
        pre100 += 100
    saveToMD("["+str(i)+".](https://www.acwing.com/problem/content/)\n\n\n\n```cpp\n```")
