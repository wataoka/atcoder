def is_lunlun(n):
    n_list = list(map(int, list(str(n))))
    for i in range(len(n_list)-1):
        if abs(n_list[i] - n_list[i+1]) >= 2:
            return False
    return True

# a[i]: i番目のルンルン数
a = []

if __name__ == "__main__":
    
    end = 222345677
    num_now =29928 

    i = end+1
    while True: 
        if len(a)+num_now == 10**5:
            break
        if is_lunlun(i):
            a.append(i)
        i+=1
    
    print(a)