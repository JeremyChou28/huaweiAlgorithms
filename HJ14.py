# @description:字符串排序：给定n个字符串，请对n个字符串按照字典序排列
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 14:31

while True:
    try:
        N=int(input())
        strlist=[]
        for i in range(N):
            string=input()
            strlist.append(string)
        for i in sorted(strlist):
            print(i)
    except:
        break