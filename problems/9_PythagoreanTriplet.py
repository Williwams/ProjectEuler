




for c in range(3,999):
    for b in range(2, 1000-c):
        for a in range(1,1001-(b+c)):
            if a < b < c and a+b+c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print(a, b, c, a*b*c)
                #break