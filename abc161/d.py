def is_lunlun(n):
    n_list = list(map(int, list(str(n))))
    for i in range(len(n_list)-1):
        if abs(n_list[i] - n_list[i+1]) >= 2:
            return False
    return True

def next_lunlun(n):

    n_list = list(map(int, list(str(n))))
    for j in range(len(n_list)-1, -1, -1):
        tmp = n_list
        tmp[j] = tmp[j]+1
        if tmp[j] > 9:
            pass
        else:

# -------------------------
K = int(input())

# a[i]: i番目のルンルン数
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if K < len(a):
    print(a[K-1])
    exit(0)

if __name__ == "__main__":
    
    while len(a) != K: 
        x = a[-1]
    
        # 1を足せばルンルン数
        if is_lunlun(x+1):
            a.append(x+1)
            continue
        
    
    
    print(a[-1])