import sys
def is_leap(a):
    if(a%400==0):
        return True
    elif(a%100!=0 and a%4==0):
        return True
    elif((a%100==0)):
        return False
    else:
        return False
year = int(input())
print(is_leap(year))