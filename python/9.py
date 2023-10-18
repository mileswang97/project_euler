ceiling = 500

for a in range(ceiling):
    for b in range(ceiling):
        c = 1000 - a - b
        if (a**2 + b**2) == c**2:
            print(a * b * c)
