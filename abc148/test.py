for i in range(2221):
    if int(list(str(i))[0]) == 5:
        print(i)

def f(n):
    if n<2:
        return 1
    return n*f(n-2)

print(f(260))