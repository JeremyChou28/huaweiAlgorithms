# @description:句子逆序：将一个英文语句以单词为单位逆序排放
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 11:54

while True:
    try:
        string=input()
        strlist=string.split(' ')
        newStr=''
        for i in range(len(strlist)):
            newStr=newStr+strlist[len(strlist)-1-i]+' '
        print(newStr)
    except:
        break