s = input()
def ispalindrome():
    t = s[::-1]
    if(t == s):
        return True
    return False
if ispalindrome() == True:
    print("It's palindrome")
else:
    print("It's not palindrome")