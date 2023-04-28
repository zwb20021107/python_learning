# -*- coding: utf-8 -*-
# @Time : 2023/4/28 22:34
# @Author : ZuoWenBin

str = " 电话：13801138823"

# 单个字符

import re


# .匹配任意字符除了/n
ret = re.match("t.o","too")
print(ret.group())
# 如果hello的⾸字符⼩写，那么正则表达式需要⼩写的h
ret = re.match("h","hello Python")
print(ret.group())
# 如果hello的⾸字符⼤写，那么正则表达式需要⼤写的H
ret = re.match("H","Hello Python")
print(ret.group())

# ⼤⼩写h都可以的情况
ret = re.match("[hH]","hello Python")
print(ret.group())
ret = re.match("[hH]","Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python","Hello Python")
print(ret.group())

# 匹配0到9的多种写法
ret = re.match("[0123456789]Hello Python","7Hello Python")
print(ret.group())
ret = re.match("[0-9]Hello Python","7Hello Python")
print(ret.group())
# 匹配0到3和5-9
ret = re.match("[0-35-9]Hello Python","7Hello Python")
print(ret.group())
ret = re.match("[0-35-9]Hello Python","4Hello Python")
#print(ret.group())
ret = re.match("嫦娥\d号","嫦娥1号发射成功")
print(ret.group())
ret = re.match("嫦娥\d号","嫦娥2号发射成功")


# 匹配多个字符

#：匹配出，⼀个字符串第⼀个字⺟为⼤写字符，后⾯都是⼩写字⺟并且这些⼩写字⺟可有可⽆
pattern = "[A-Z][a-z]*"
ret = re.match("[A-Z][a-z]*","M")
print(ret.group())
ret = re.match("[A-Z][a-z]*","MnnM")
print(ret.group())
ret = re.match("[A-Z][a-z]*","Aabcdef")
print(ret.group())
#匹配出，变量名是否有效
pattern = "[a-zA-Z_]+[\w]*"
names = ["name1", "_name", "2_name", "__name__"]
for name in names:
    ret = re.match("[a-zA-Z_]+[\w]*",name)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s ⾮法" % name)
#匹配出，0到99之间的数字
ret = re.match("[1-9]?[0-9]","7")
print(ret.group())
ret = re.match("[1-9]?\d","33")
print(ret.group())
# 这个结果并不是想要的，利⽤$才能解决
ret = re.match("[0-9]?\d","09")
print(ret.group())
ret = re.match("[a-zA-Z0-9_]{6}","12a3g45678")
print(ret.group())
#匹配出，8到20位的密码，可以是⼤⼩写英⽂字⺟、数字、下划线
pattern = "[a-zA-Z0-9_]{8, 20}"
ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
print(ret.group())

# 匹配开头结尾
#匹配163.com的邮箱地址
pattern="[\w]{4, 20}@163\.com$"
email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
for email in email_list:
    ret = re.match("[\w]{4,20}@163\.com$", email)
    if ret:
        print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
    else:
        print("%s 不符合要求" % email)


# 匹配分组
#匹配出0-100之间的数字

# 举例 |
pattern = "[1-9]?\d$|100"
ret = re.match("[1-9]?\d$|100","8")
print(ret.group()) # 8
ret = re.match("[1-9]?\d$|100","100")
print(ret.group()) # 100

# 举例()

#需求：匹配出163、126、qq邮箱
pattern = "[\w]{4, 20}@(163|126|qq)\.com"


# 举例：\number
# 匹配数字代表的组合。每个括号是一个组合，组合从1开始编号。比如 (.+) \1 匹配 'the the' 或者 '55 55', 但不会匹配 'thethe' (注意组合后面的空格)。这个特殊序列只能用于匹配前面99个组合。如果 number 的第一个数位是0， 或者 number 是三个八进制数，它将不会被看作是一个组合，而是八进制的数字值。在 '[' 和 ']' 字符集合内，任何数字转义都被看作是字符。

# 需求：匹配出<html>hh</html>
result = re.match("<([a-zA-Z1-6]{4})>.*</\\1>", "<html>hh</html>")
print(result.group())


# 需求：匹配出<html><h1>hh</h1></html>
result = re.match("<([a-zA-Z1-6]{4})><([a-zA-Z1-6]{2})>.*</\\2></\\1>", "<html><h1>hh</h1></html>")
result = re.match("<(?P<html>[a-zA-Z1-6]{4})><(?P<h1>[a-zA-Z1-6]{2})>.*</(?P=h1)></(?P=html)>", "<html><h1>hh</h1></html>")\

print(result.group())


# re.findall函数
str = "13517923238"

result = re.findall('3', str)
print(result)


# re.search函数
import re

str = "阅读次数为9999"

ret = re.search(r"\d", str)

print(ret.group())


# re.finditer函数
import re
it = re.finditer("\d+", "12a32bc43jf3")

for i in it:
    print(i.group())
