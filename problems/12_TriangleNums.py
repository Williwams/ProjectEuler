

def getDivisors(num):
    out = [1]
    cur = 2
    while cur <= num ** 1/2:
        if num % cur == 0:
            out.append(cur)
        cur += 1
    out.append(num)
    return out

x=6
maxdivs = 0
while True:
    cursum = sum(range(x))
    newdivs = len(getDivisors(cursum))
    if newdivs > maxdivs:
        maxdivs = newdivs
        print(newdivs, x, cursum)
    if newdivs>=500:
        print(cursum)
        print(getDivisors(cursum))
        break
    x+=1