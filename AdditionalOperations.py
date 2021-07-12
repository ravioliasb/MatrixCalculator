def modulo(x, y):
    q = x//y
    remainder = x - y * q
    return remainder


def gcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            gcd_num = i
    return gcd_num


def lcm(x, y):
    lcm_num = (x * y) / gcd(x, y)
    return int(lcm_num)


def factorial(x):
    if x == 1:
        return x
    elif x < 1:
        return "NA"
    else:
        return x * factorial(x - 1)


def choose(x, y):
    if y > x:
        return "NA"
    else:
        return int(factorial(x) / (factorial(y) * factorial(x - y)))


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x < 2:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def n_primes(num):
    for n in range(1, num):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)


def maximum(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    elif x == y:
        return x


def minimum(x, y):
    if x < y:
        return x
    elif x > y:
        return y
    elif x == y:
        return x


def permutation(x, y):
    return int(factorial(x) / factorial(x-y))


def parity(x):
    if x % 2 == 0:
        return "Even"
    elif not x % 2 == 0:
        return "Odd"


def factors(x):
    fact_arr = []
    for integers in range(1, x+1):
        if x % integers == 0:
            fact_arr.append(-integers)
            fact_arr.append(integers)
    return fact_arr
