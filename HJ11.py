# @description:数字颠倒：输入一个整数，将这个整数以字符串的形式逆序输出
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 11:50

while True:
    try:
        N=int(input())
        lt=[]
        newNum=''
        while N/10!=0:
            lt.append(int(N%10))
            N//=10
        for i in range(len(lt)):
            newNum+=str(lt[i])
        print(newNum)
    except:
        break
