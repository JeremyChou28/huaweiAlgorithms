# @description:购物单：动态规划
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 14:43

# while True:
#     try:
#         Money_Count=input()
#         Money=int(Money_Count.split(' ')[0])
#         Count=int(Money_Count.split(' ')[1])
#         Objlist=[]
#         moneylist=[]
#         if Money>=32000 or Count>=60:
#             print("输入非法")
#         else:
#             for i in range(Count):
#                 Obj=input()
#                 Obj=Obj.split(' ')
#                 for j in range(len(Obj)):
#                     Obj[j]=int(Obj[i])
#                 if Obj[0]>=10000 or Obj[1]<1 or Obj[1]>5 or Obj[2]<0:
#                     print("输入非法")
#                 else:
#                     Objlist.append(Obj)
#             for i in range(Count):
#                 for j in range(Count):
#                     if Objlist[i][0]+Objlist[j][0]<=Money:
#     except:
#         break
n, m = map(int,input().split())
primary, annex = {}, {}
for i in range(1,m+1):
    x, y, z = map(int, input().split())
    if z==0:
        primary[i] = [x, y]
    else:
        if z in annex:
            annex[z].append([x, y])
        else:
            annex[z] = [[x,y]]
dp = [0]*(n+1)
for key in primary:
    w, v= [], []
    w.append(primary[key][0])#1、主件
    v.append(primary[key][0]*primary[key][1])
    if key in annex:#存在附件
        w.append(w[0]+annex[key][0][0])#2、主件+附件1
        v.append(v[0]+annex[key][0][0]*annex[key][0][1])
        if len(annex[key])>1:#附件个数为2
            w.append(w[0]+annex[key][1][0])#3、主件+附件2
            v.append(v[0]+annex[key][1][0]*annex[key][1][1])
            w.append(w[0]+annex[key][0][0]+annex[key][1][0])#4、主件+附件1+附件2
            v.append(v[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
    for j in range(n,-1,-10):#物品的价格是10的整数倍
        for k in range(len(w)):
            if j-w[k]>=0:
                dp[j] = max(dp[j], dp[j-w[k]]+v[k])
print(dp[n])