import numpy as np
from utils.sequences import primes

primes_list = primes(2000000)

print(np.sum(primes_list))