# @description:参数解析
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/30 10:16

while True:
    try:
        s = input()
        flag = 0
        start = end = i = sum = 0
        res = []
        while i < len(s):
            if s[i] == ' ':
                sum += 1
                end = i
                res.append(s[start:end])
                start = end + 1

            if s[i] == '"':
                start = i + 1
                flag = 1
                while flag == 1:
                    i += 1
                    if s[i] == '"':
                        end = i
                        flag = 0
                        res.append(s[start:end])
                        end = i = i + 1
                        start = end + 1
            i += 1
        if end < len(s):
            res.append(s[start:])
        print(len(res))
        for i in res:
            print(i)
    except Exception:
        break