import sympy

primes_below_a_million = list(sympy.sieve.primerange(0,1000000))

def rotate(num):
    string = str(num)
    return int(string[1::] + string[0])

def circle_prime(n: int) -> bool:
    length = len(str(n))
    for i in range(length):
        n = rotate(n)
        if n not in primes_below_a_million:
            return False
    return True 

def find_circle_primes(n: int = 1000000):
    

circle_primes_list = []