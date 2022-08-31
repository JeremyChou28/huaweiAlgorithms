# @description:取近似值:接受一个正浮点数值，输出该数值的近似整数值
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 10:28

while True:
    try:
        f=float(input())
        if int(f*10)%10>=5:
            print(int(f)+1)
        else:
            print(int(f))
    except:
        break