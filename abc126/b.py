s = input()

ff = int(s[:2])
bb = int(s[2:])

if (ff>=1 and ff<=12) and (bb>=1 and bb<=12):
    print("AMBIGUOUS")
elif (ff>=1 and ff<=12):
    print("MMYY")
elif (bb>=1 and bb<=12):
    print("YYMM")
else:
    print("NA")