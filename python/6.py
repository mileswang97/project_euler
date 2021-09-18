from utils.sequences import squares, powers
import numpy as np

square_list = squares(100)
sum_list = powers(100,1)

diff = (np.sum(sum_list))**2 - np.sum(square_list)

print(diff)