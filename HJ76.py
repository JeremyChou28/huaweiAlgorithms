# @description:尼科彻斯定理
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/30 14:40

while True:
    try:
        m=int(input())
        N=m**3
        strlist=[]
        if m == 1:
            strlist.append('1')
        else:
            for i in range(m):
                strlist.append(str(m**2-m+1+i*2))
        print('+'.join(strlist))
    except Exception:
        break