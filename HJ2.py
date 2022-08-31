# @description:计算某字母出现次数
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/26 21:30

string=input()
letter=input()

if len(string)>=500 or len(string)==0:
    print("输入字符串非法")
else:
    strlist=[ch for ch in string]
    count=0
    for i in range(len(string)):
        if strlist[i]==letter.lower() or strlist[i]==letter.upper():
            count+=1
    print(count)