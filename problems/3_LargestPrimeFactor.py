val = 600851475143
x = 2
while x < val ** 1/x:
    if val % x == 0:
        val = val // x
        print(f'factor: {x}')
        x=1
    x+=1

print(f'top factor {val}')