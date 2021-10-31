from utils.sequences import triangles
from utils.utils import list_of_divisors

first_five_hundred = next((x for x in triangles(100000) if len(list_of_divisors(x)) > 500), None)

print(first_five_hundred)