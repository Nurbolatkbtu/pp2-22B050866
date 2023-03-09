import re
s = "abappleadvicebabewjdiwje"
pattern = re.search(r'[a].*[b$]',s)
print(pattern.group())