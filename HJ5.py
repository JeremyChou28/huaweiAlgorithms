# @description:进制转换:接受一个十六进制的数，输出该数值的十进制表示。
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 9:06

while True:
    try:
        string=input()
        if len(string)==0:
            print("字符串非法")
        else:
            DecimalStr=int(string,16)
            print(DecimalStr)
    except:
        break