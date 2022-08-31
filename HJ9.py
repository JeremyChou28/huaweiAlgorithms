# @description:提取不重复的整数:输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 11:13

while True:
    try:
        N=int(input())
        lt=[]
        newNum=''
        while N/10!=0:
            if N%10 not in lt:
                lt.append(int(N%10))
            N//=10
        for i in range(len(lt)):
            newNum+=str(lt[i])
        newNum=int(newNum)
        print(newNum)
    except:
        break