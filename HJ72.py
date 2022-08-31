# @description:百钱买百鸡问题
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/29 22:00

def GetResult():
    Resultlist=[]
    money=100
    for chickenFather in range(20):
        for chickenMother in range(34):
            for chickenChildren in range(0,100,3):
                if chickenFather*5+chickenMother*3+chickenChildren/3*1==100 and chickenFather+chickenMother+chickenChildren==100:
                    Result = []
                    Result.append(chickenFather)
                    Result.append(chickenMother)
                    Result.append(chickenChildren)
                    Resultlist.append(Result)

    return Resultlist

while True:
    try:
        N=input()
        if len(N)!=0:
            Resultlist=GetResult()
            for i in Resultlist:
                print(str(i[0])+' '+str(i[1])+' '+str(i[2]))
        else:
            print("失败")
    except Exception:
        break