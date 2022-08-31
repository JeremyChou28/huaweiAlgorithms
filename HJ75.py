# @description:公共子串计算
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/30 11:23

while True:
    try:
        a=input()
        b=input()
        if len(a)>len(b):
            a,b=b,a
        maxlength=0
        i=0
        while i+maxlength<len(a):
            while i+maxlength<len(a) and a[i:i+maxlength+1] in b:
                maxlength+=1
            i+=1
        print(maxlength)
    except Exception:
        break