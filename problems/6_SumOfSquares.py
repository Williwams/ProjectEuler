


r = range(1,101)
sumofsquares = sum([x**2 for x in r])
squareofsums = sum([x for x in r])**2

print(sumofsquares, squareofsums, squareofsums-sumofsquares)