def filter_prime(arr):
    temp = []
    for i in arr:
        prime = True
        if int(i) < 2:
            continue
        for j in range(2, int(i) - 1):
            if int(i) % j == 0:
                prime = False
        if prime == True:
            temp.append(int(i))
    return temp
a = input().split()
print(filter_prime(a))