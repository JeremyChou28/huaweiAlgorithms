# @description:杨辉三角的变形
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/29 9:54

while True:
    try:
        N=int(input())
        if N==0 or N>1000000000:
            print("输入错误")
        else:
            if N==1 or N==2:
                print(-1)
            elif N%2==1:
                print(2)
            elif N%4==0:
                print(3)
            else:
                print(4)
    except Exception:
        break