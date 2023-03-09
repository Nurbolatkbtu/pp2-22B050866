import re
s = ['a', 'babb', 'abb', 'abbb', 'abbbb', 'abbbbb', "ab"]
a = r"[b]{2,3}\b"
for i in s:
    if re.search(a,i):
        print(i)
    else:
        pass