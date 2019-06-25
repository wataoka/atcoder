from datetime import datetime

s = str(input())

year = int(s[:4])
month = int(s[5:7])
day = int(s[8:])

if datetime(2019, 4, 30) < datetime(year, month, day):
    print("TBD")
else:
    print("Heisei")

