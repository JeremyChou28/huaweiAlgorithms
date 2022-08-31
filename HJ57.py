# @description:高精度整数加法
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/29 10:08

# while True:
#     try:
#         str1=input()
#         str2=input()
#         if len(str1)>10000 or len(str1)==0 or len(str2)>10000 or len(str2)==0:
#             print("输入非法")
#         else:
#             alist=list(str1)[::-1]
#             blist=list(str2)[::-1]
#             clist=[]
#             result=''
#             maxlength=max(len(alist),len(blist))
#             if len(alist)<maxlength:
#                 templist=['0']*(maxlength-len(alist))
#                 alist=alist+templist
#             elif len(blist)<maxlength:
#                 templist=['0']*(maxlength-len(blist))
#                 blist=blist+templist
#             for i in range(maxlength):
#                 sum=int(alist[i])+int(blist[i])
#                 if sum<=9:
#                     clist.append(str(sum))
#                 elif sum>9 and i<=maxlength-2:
#                     alist[i+1]=str(int(alist[i+1])+1)
#                     clist.append(str(sum%10))
#                 elif sum>9 and i==maxlength-1:
#                     clist.append(str(sum%10))
#                     clist.append(str(1))
#             for i in clist[::-1]:
#                 result+=i
#             print(result)
#     except Exception:
#         break

while True:
    try:
        x1=int(input())
        x2=int(input())
        print(x1+x2)
    except Exception:
        break