import re
s = "I want to eat some rice with meat, maybe, fish."
pattern =re.sub("[ ,.]", ":", s)
print(pattern)