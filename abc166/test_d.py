for i in range(1, 1000):
    x = (i+1)**5 - i**5
    x = str(x)
    if len(x) == 10:
        print(i)
        quit()