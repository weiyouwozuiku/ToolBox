#!/usr/bin/env python
# coding=utf-8
import sys
from workflow import Workflow3

def show(value):
    result=[]
    resultStr=''
    for i in range(len(value),0,-4):
        result.append(','+value[(i-4 if i-4>=0 else 0):i])
    result.reverse()
    result[0]=result[0][1:]
    for i in result:
        resultStr+=i
    return resultStr

#除了10进制以外，展示时去掉前缀，即str[2:]

def binShow(num):
    binStr=bin(num)
    return show(binStr[2:])

#python2中的oct()返回以‘0’为前缀的字符串，因此特判[1:]
def octShow(num):
    octStr=oct(num)
    return show(octStr[1:])

def decShow(num):
    decStr=str(num)
    return show(decStr)

def hexShow(num):
    hexStr=hex(num)
    return show(hexStr[2:])

    

def conversionFromBin(num):
    return {
        'title': octShow(num),
        'subtitle': '八进制',
        'arg': oct(num),
        'valid': True
    },{
        'title': decShow(num),
        'subtitle': '十进制',
        'arg': str(num),
        'valid': True
    },{
        'title': hexShow(num),
        'subtitle': '十六进制',
        'arg': hex(num),
        'valid': True
    }

def conversionFromDec(num):
    return {
        'title': binShow(num),
        'subtitle': '二进制',
        'arg': bin(num),
        'valid': True
    },{
        'title': octShow(num),
        'subtitle': '八进制',
        'arg': oct(num),
        'valid': True
    },{
        'title': hexShow(num),
        'subtitle': '十六进制',
        'arg': hex(num),
        'valid': True
    }

def conversionFromOct(num):
    return {
        'title': binShow(num),
        'subtitle': '二进制',
        'arg': bin(num),
        'valid': True
    },{
        'title': decShow(num),
        'subtitle': '十进制',
        'arg': str(num),
        'valid': True
    },{
        'title': hexShow(num),
        'subtitle': '十六进制',
        'arg': hex(num),
        'valid': True
    }

def conversionFromHex(num):
    return {
        'title': binShow(num),
        'subtitle': '二进制',
        'arg': bin(num),
        'valid': True
    },{
        'title': octShow(num),
        'subtitle': '八进制',
        'arg': oct(num),
        'valid': True
    },{
        'title': decShow(num),
        'subtitle': '十进制',
        'arg': str(num),
        'valid': True
    }
    
def getValue(num):
    if len(num)==1:
        return int(num),10
    else:
        try:
            if num[:2]=='0x' or num[:2]=='0X':
                return int(num,16),16
            if num[:2]=='0o' or num[:2]=='0O':
                return int(num,8),8
            if num[:2]=='0b' or num[:2]=='0B':
                return int(num,2),2
            return int(num),10
        except:
            raise Exception,"输入数据有误："+num+"，请重新输入！"

def main():
    num=sys.argv[1]
    value=0
    wf=Workflow3()
    try:
        if num[0]<'0' or num[0]>'9':
            raise Exception,"错误的数据输入："+str(num)
        elif len(num)==2 :
            if num[:2]=='0x' or num[:2]=='0X' :
                raise Exception,"请继续输入一个16进制数..."
            if num[:2]=='0o' or num[:2]=='0O' :
                raise Exception,"请继续输入一个8进制数..."
            if num[:2]=='0b' or num[:2]=='0B' :
                raise Exception,"请继续输入一个2进制数..."
            value,base=getValue(num)
        else:
            value,base=getValue(num)
    except Exception,err: 
        wf.add_item(str(err))
        wf.send_feedback()
        exit()
    switch={
        2: conversionFromBin,
        8: conversionFromOct,
        10:conversionFromDec,
        16:conversionFromHex
    }
    result=switch[base](value)
    for item in result:
        wf.add_item(**item)
    wf.send_feedback()


if __name__=="__main__":
    main()