import math


# 质数不包括1
def func_get_prime(n):
    # return filter(lambda x: not [x % i for i in range(2, int(math.sqrt(x)) + 1) if x % i == 0], range(2, n + 1))
    # return (" ".join("%s" % i for i in range(2, n) if not [y for y in range(2, int(math.sqrt(i))+1) if i % y == 0])).split()
    # print(i for i in range(n - 1, 2) if not [y for y in range(2, int(math.sqrt(i)) + 1) if i % y == 0])
    while n > 2:
        if not [y for y in range(2, int(math.sqrt(n)) + 1) if n % y == 0]:
            return n
        n -= 1




print(func_get_prime(100))
