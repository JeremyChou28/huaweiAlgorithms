# @description:字符串反转：接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 11:52

while True:
    try:
        string=input()
        strlist=list(string)
        newStr=''
        for i in range(len(strlist)):
            newStr+=strlist[len(strlist)-1-i]
        print(newStr)
    except:
        break