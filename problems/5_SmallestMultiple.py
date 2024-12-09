




def isDivisible(num):
    for i in range(2,21):
        if num % i != 0:
            return False
    return True


x = 20
while True:
    if not isDivisible(x):
        x+=20
    else:
        print(x)
        break