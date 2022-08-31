# @description:放苹果
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/29 15:40

def f(m,n):
    # m为苹果数量，n为盘子数量
    if m==0 or n==1:
        return 1
    elif m<n:
        return f(m,m)
    else:
        return f(m,n-1)+f(m-n,n)
while True:
    try:
        string=input()
        appleNum=int(string.split()[0])
        plateNum=int(string.split()[1])
        if appleNum<0 or appleNum>10 or plateNum<0 or plateNum>10:
            print("输入非法")
        else:
            print(f(appleNum,plateNum))
    except Exception:
        break