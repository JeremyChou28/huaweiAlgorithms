# @description:完全数计算
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/29 10:00

while True:
    try:
        N=int(input())
        if N<=0 or N>500000:
            print("输入错误")
        else:
            alist=[]
            count=0
            for i in range(1,N+1):
                for j in range(1,i):
                    if i%j==0:
                        alist.append(j)
                if sum(alist)==i:
                    count+=1
                alist.clear()
            print(count)
    except Exception:
        break