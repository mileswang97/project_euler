def collatz_chain(n: int, n_list: list) -> list:
    if not n_list:
        n_list.append(n)
    if n == 1:
        return n_list
    if n % 2 == 0:
        n_list.append(int(n / 2))
        return collatz_chain(int(n / 2), n_list)
    if n % 2 == 1:
        n_list.append(3 * n + 1)
        return collatz_chain(3 * n + 1, n_list)


i_temp = 0
length_temp = 0
for i in range(1, 1000000):
    collatz_length = len(collatz_chain(i, []))
    if collatz_length > length_temp:
        print("changing i", i, collatz_length)
        i_temp = i
        length_temp = collatz_length

print(i_temp)
print(length_temp)
