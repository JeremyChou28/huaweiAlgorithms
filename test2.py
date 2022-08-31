# @description:
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/30 20:51

import sys
if __name__ == "__main__":

    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    s1 = list(map(int, line1.split()))
    s2=list(map(int, line2.split()))
    alist=[]
    for i in range(s1[-1]-s1[0]):
        alist.append(s1[0])