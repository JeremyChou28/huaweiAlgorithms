# @description:质数因子
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/27 9:11

# while True:
#     try:
#         N=int(input())
#         i=2
#         while i<=N:
#             while N%i==0:
#                 N = N / i
#                 print(str(i),end=' ')
#             i+=1
#     except:
#         break
import math
def is_prime_number(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        continue
    return True

while True:
    try:
        lt=[]
        N=int(input())
        if is_prime_number(N)==True:
            lt.append(N)
        else:
            for i in range(2,int(N/2)+1):
                if is_prime_number(i)==True:
                    while N%i==0:
                        N = N // i
                        lt.append(i)
                    if is_prime_number(N)==True:
                        lt.append(N)
                        break
        for i in sorted(lt):
            print(i,end=' ')
    except:
        break
# import math
# def is_prime_number(num):
#     if num == 1:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#         continue
#     return True
#
# while True:
#     try:
#         lt = []
#         number = int(input())
#         if is_prime_number(number):
#             lt.append(number)
#         else:
#             for i in range(2, int(number / 2) + 1):
#                 while number % i == 0:
#                     lt.append(i)
#                     number = number // i
#                 if is_prime_number(number):
#                     lt.append(number)
#                     break
#         for i in sorted(lt):
#             print(i, end = ' ')
#
#     except:
#         break