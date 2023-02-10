from itertools import permutations
s = str(input())
t = permutations(s)
for i in t:
    print(i)