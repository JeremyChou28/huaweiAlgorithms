# @description:删除字符串中出现次数最少的字符
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/28 16:53

while True:
    try:
        string=input()
        if len(string)>20:
            print("输入错误")
        else:
            dict1={}
            strlist=list(string)
            for i in range(len(strlist)):
                if strlist[i] not in dict1.keys():
                    dict1[strlist[i]]=1
                else:
                    dict1[strlist[i]]+=1
            minvalue = min(dict1.values())
            for key,value in dict1.items():
                if value==minvalue:
                    for i in strlist:
                        if i==key:
                            strlist.remove(i)
            newStr=''
            for i in strlist:
                newStr+=i
            print(newStr)
    except Exception:
        break