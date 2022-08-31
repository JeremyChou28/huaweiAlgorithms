# @description:生成N个随机数，完成去重和排序
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/26 21:42

# import numpy as np
#
# while True:
#     N=int(input())
#     if N>1000 or N==0:
#         print("输入非法")
#     else:
#         randNumlist=np.random.randint(1,1000,size=N)
#         alist=np.unique(randNumlist)
#         sortlist=np.sort(alist)
#         for i in sortlist:
#             print(i)
while True:
    try:
        N=int(input())
        if N>1000 or N==0:
            print("输入非法")
        else:
            randNumlist=[]
            for i in range(N):
                # randnum=random.randint(1,1000)
                randnum=int(input())
                randNumlist.append(randnum)
            aset=set(randNumlist)
            alist=list(aset)
            sortlist=sorted(alist)
            for i in sortlist:
                print(i)
    except:
        break

# while True:
#     try:
#         n = int(input())
#         set1 = set({})
#         for i in range(n):
#             set1.add(int(input()))
#
#         nums = list(set1)
#         nums.sort()
#         for i in nums:
#             print(i)
#     except:
#         break