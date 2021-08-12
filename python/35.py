import sympy

def rotate(str):
    return str[1:] + str[0]

def circle_prime(num, primes_list) -> bool:
    length = len(str(num))
    strnum = str(num)
    num_list = []
    for i in range(length):
        strnum = rotate(strnum)
        num_list.append(strnum)
    print(num_list)
    for value in num_list:
        value = int(value)
        if value not in primes_list:
            return False
    return True 

def find_circle_primes(n: int = 1000000):
    master_list = []
    primes_set = set(sympy.sieve.primerange(0,n))
    for prime in primes_set:
        if circle_prime(prime, primes_set):
            master_list.append(prime)
    print(master_list)
    return master_list

print(len(find_circle_primes()))