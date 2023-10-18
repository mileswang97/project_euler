def fib(n):
    fib_list = []
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        fib_list.append(a)
    return fib_list


def sum_fib_even():
    sum = 0
    fib_list = fib(4000000)
    for num in fib_list:
        if num % 2 == 0:
            sum += num
    print(sum)
    return


sum_fib_even()
