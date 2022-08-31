# @description:字符个数统计:计算字符串中含有的不同字符的个数
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 11:32

while True:
    try:
        string=input()
        strlist=list(string)
        aset=set(strlist)
        print(len(aset))
    except:
        break