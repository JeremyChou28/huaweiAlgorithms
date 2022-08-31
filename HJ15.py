# @description:求int型正整数在内存中存储时1的个数
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 14:35

while True:
    try:
        N=int(input())
        count=0
        while N/2!=0:
            if int(N%2)==1:
                count+=1
            N//=2
        print(count)
    except:
        break