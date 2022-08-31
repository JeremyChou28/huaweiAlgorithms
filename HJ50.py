# @description:四则运算
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/29 9:06

import re
def jisuan(s):
    s=s.replace("+-","-").replace("--","+").replace("*-","a").replace("/-","b")
    if s[0]=="-":
        s="0"+s
    fu=re.findall(r"[*+-/ab]",s)[::-1]
    mum=list(map(int,re.split(r'[*+-/ab]',s)))[::-1]
    l,ll,lll=[],["+","-"],["*","/"]
    for i in range(len(fu)-1,-1,-1):
        if fu[i] =="a":
            mum.insert(i,-mum.pop(i+1)*mum.pop(i))
            del fu[i]
        elif fu[i] =="b":
            mum.insert(i,-mum.pop(i+1)/mum.pop(i))
            del fu[i]
        elif fu[i] =="*":
            mum.insert(i,mum.pop(i+1)*mum.pop(i))
            del fu[i]
        elif fu[i] =="/":
            mum.insert(i,mum.pop(i+1)/mum.pop(i))
            del fu[i]
    for i in range(len(fu)-1,-1,-1):
        if fu[i] =="+":
            mum.insert(i,mum.pop(i+1)+mum.pop(i))
        elif fu[i] =="-":
            mum.insert(i,mum.pop(i+1)-mum.pop(i))
    return str(int(mum[0]))

def kuohao(kk,b,s):
    l,ll,lll="","",[]
    for i in range(len(s)):
        if s[i]==kk:
            ll+=s[i]
            lll+=[len(ll)]
        elif s[i]==b:
            k=lll.pop(-1)
            if len(lll)>=1:
                ll=ll[0:k-1]+jisuan(ll[k:])
            else:
                l+=jisuan(ll[k:])
                ll=''
        elif len(lll)==0:
            l+=s[i]
        else:
            ll+=s[i]
    return l

while True:
    try:
        print(int(jisuan(kuohao("{","}",kuohao("[","]",kuohao("(",")",input()))))))
    except:
        break
