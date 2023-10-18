import sympy

number = 600851475143

primelist = list(sympy.sieve.primerange(0, 100000))

templist = []
for prime in primelist:
    if number % prime == 0:
        templist.append(prime)
        number = number / prime

templist = sorted(templist)
print(templist)
