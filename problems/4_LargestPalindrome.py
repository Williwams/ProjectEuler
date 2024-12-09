def isPalindrome(num):
    num = str(num)
    for x in range((len(num)+1)//2):
        if num[x] != num[-(x+1)]:
            return False
    return True


top = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if i*j > top and isPalindrome(i*j):
            top = i*j

print(top)
