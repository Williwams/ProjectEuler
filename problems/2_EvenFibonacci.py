f1 = 1
f2 = 2
total = 0
highest = 4000000
while f1 <= highest and f2 <= highest:
    if f1 <= highest and f1 % 2 == 0:
        total += f1
    if f2 <= highest and f2 % 2 == 0:
        total += f2
    f1, f2 = f2+f1, 2*f2+f1
    
                
print(total)