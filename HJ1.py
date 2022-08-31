# @description:计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/26 16:55

# while True:
#     try:
#         in_str = input()
#         if len(in_str) > 5000 or len(in_str) == 0:
#             raise Exception
#
#         last = in_str.strip().split(" ")[-1]
#         leng = len(last)
#         print(leng)
#         break
#     except Exception:
#         print("字符串非空且长度小于5000，请再次输入：")

string=input()
if len(string)>=5000 or len(string)==0:
    print("输入字符串非法")
else:
    word=string.split(" ")[-1]
    wordLength=len(word)
    print(wordLength)