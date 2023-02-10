def histogram(x):
    for i in x:
        while i > 0:
            print("*", end = "")
            i -= 1
        print('')
histogram([4, 9, 7])
