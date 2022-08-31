# @description:合并表记录：将相同索引的数值进行求和运算，输出按照key值升序进行输出
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 10:40

while True:
    try:
        N=int(input())
        dict1 = {}
        key_value_list=[]
        for i in range(N):
            key_value_str=input()
            key_value_list.append(key_value_str)
        for i in range(N):
            key_value=key_value_list[i].split(' ')
            key=int(key_value[0])
            value=int(key_value[1])
            if key not in dict1.keys():
                dict1[key]=value
            else:
                dict1[key]+=value
        lt=sorted(dict1.items(),key=lambda d:d[0])
        for i in lt:
            string=str(i[0])+' '+str(i[1])
            print(string)
    except:
        break