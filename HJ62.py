# @description:查找输入整数二进制中1的个数
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/29 19:32

while True:
    try:
        N=int(input())
        count=0
        while N!=0:
            if N%2!=0:
                count+=1
            N//=2
        print(count)
    except Exception:
        break