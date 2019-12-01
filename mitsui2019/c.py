x = input()
s = list(x)
x = int(x)

if len(s) < 3:
    print(0)
else:
    xx = int(s[-2]+s[-1])
    num_item = xx//5
    if xx%5 != 0:
        num_item += 1
    
    hun = int(''.join(s[0:-2]))
    if hun < num_item:
        print(0)
    else:
        print(1)