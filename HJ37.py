# @description:统计每个月兔子的总数
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/28 20:31

def fN(N):
    if N==1 or N==2:
        return 1
    return fN(N-1)+fN(N-2)

while True:
    try:
        N=int(input())
        print(fN(N))

    except Exception:
        break