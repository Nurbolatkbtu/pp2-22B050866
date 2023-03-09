import re
a = "a ab abb abbb"
print(re.findall("a[b]*",a))