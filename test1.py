# @description:
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/30 19:02

import sys
if __name__ == "__main__":
    # 读取第一行的N
    n = int(sys.stdin.readline().strip())
    line=sys.stdin.readline().strip()
    numList=list(map(int, line.split()))
    scorelist1= [1] * n
    scorelist2=[1]*n
    minNum=min(numList)
    minindex=numList.index(minNum)
    leftlist=(numList[0:minindex+1:1])[::-1]+(numList[minindex+1::1])[::-1]
    rightlist=numList[minindex::1]+numList[0:minindex:1]
    for leftindex in range(len(leftlist)-1):
        if leftlist[leftindex+1]>leftlist[leftindex]:
            scorelist1[leftindex+1]=scorelist1[leftindex]+1
        elif leftlist[leftindex]==leftlist[leftindex+1]:
            scorelist1[leftindex +1]=scorelist1[leftindex]
        else:
            scorelist1[leftindex+1]=1
    for rightindex in range(len(rightlist) - 1):
        if rightlist[rightindex+1] > rightlist[rightindex]:
            scorelist2[rightindex +1] =scorelist2[rightindex]+1
        elif rightlist[rightindex +1] == rightlist[rightindex]:
            scorelist2[rightindex +1] = scorelist2[rightindex]
        else:
            scorelist2[rightindex +1]= 1
    resultlist1=(scorelist1[1::1])[::-1]+scorelist1[0:1:1]
    resultlist2=scorelist2[1::1]+scorelist2[0:1:1]
    scorelist=[]
    for i in range(len(rightlist)):
        scorelist.append(max(resultlist1[i],resultlist2[i]))
    print(sum(scorelist))