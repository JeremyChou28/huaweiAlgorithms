# @description:计算日期到天数转换
# @author:JianpingZhou
# @company:Shandong University
# @Time:2021/6/29 22:16

def is_Run_Year(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    else:
        return False

while True:
    try:
        string=input()
        pingyear=[31,28,31,30,31,30,31,31,30,31,30,31]
        date=string.split(' ')
        year=int(date[0])
        month=int(date[1])
        day=int(date[2])
        daysum=0
        if is_Run_Year(year) and month>2:
            for i in range(month-1):
                daysum+=pingyear[i]
            daysum+=day+1
        else:
            for i in range(month-1):
                daysum+=pingyear[i]
            daysum+=day
        print(daysum)

    except Exception:
        break