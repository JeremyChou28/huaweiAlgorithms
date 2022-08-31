# @description:汽水瓶：
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/28 16:32

while True:
    try:
        n=int(input())
        if n>100:
            print("输入非法")
        elif n==0:
            raise Exception
        else:
            count=0
            temp=n//3
            while temp!=0:
                rem=n%3
                n=rem+temp
                count+=temp
                temp=n//3
                if n==2:
                    count+=1
            print(count)
    except Exception:
        break