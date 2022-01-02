#!/usr/bin/env python
# coding=utf-8
import sys
from workflow import Workflow3


def conversionFrom0b(num):
    return {
        'title': oct(num),
        'subtitle': '八进制',
        'arg': oct(num),
        'valid': True
    },{
        'title': str(num),
        'subtitle': '十进制',
        'arg': str(num),
        'valid': True
    },{
        'title': hex(num),
        'subtitle': '十六进制',
        'arg': hex(num),
        'valid': True
    }

def conversionFrom0(num):
    return {
        'title': bin(num),
        'subtitle': '二进制',
        'arg': bin(num),
        'valid': True
    },{
        'title': oct(num),
        'subtitle': '八进制',
        'arg': oct(num),
        'valid': True
    },{
        'title': hex(num),
        'subtitle': '十六进制',
        'arg': hex(num),
        'valid': True
    }

def conversionFrom0o(num):
    return {
        'title': bin(num),
        'subtitle': '二进制',
        'arg': bin(num),
        'valid': True
    },{
        'title': str(num),
        'subtitle': '十进制',
        'arg': str(num),
        'valid': True
    },{
        'title': hex(num),
        'subtitle': '十六进制',
        'arg': hex(num),
        'valid': True
    }

def conversionFrom0x(num):
    return {
        'title': bin(num),
        'subtitle': '二进制',
        'arg': bin(num),
        'valid': True
    },{
        'title': oct(num),
        'subtitle': '八进制',
        'arg': oct(num),
        'valid': True
    },{
        'title': str(num),
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
        2: conversionFrom0b(value),
        8: conversionFrom0o(value),
        10:conversionFrom0(value),
        16:conversionFrom0x(value)
    }
    result=switch[base]
    for item in result:
        wf.add_item(**item)
    wf.send_feedback()


if __name__=="__main__":
    main()
    sys.exit(wf.run(main))