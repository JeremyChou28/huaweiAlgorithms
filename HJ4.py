# @description:字符串分隔
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 8:42

def cut(obj, sec):
    return [obj[i:i+sec] for i in range(0,len(obj),sec)]

while True:
    try:
        string=input()
        if len(string)==0:
            print("字符串非法")
        elif len(string)<=8:
            string=string+(8-len(string))*str(0)
            print(string)
        else:
            strlist=cut(string,8)
            if len(strlist[-1])<8:
                strlist[-1]=strlist[-1]+(8-len(strlist[-1]))*str(0)
            for i in strlist:
                print(i)
    except:
        break
# oswgkjwvstbgfzszdoemlpvtoqeautekdfwpezdfxatvcyskrisiqcjynmtwcfmzzuseyaxanc
# guwldvzrsfurobidegiyazkggfpgmyhlrbfjrjerrbnjdenrdxjfmrhtumfdsedkcmthphgavzxlmpcpwbkwsvplhmkbkgkw