import math
from time import perf_counter
from numba import njit


@njit(fastmath=True)
def is_prime(num):
    if num == 2:
        return True
    if num <=1 or not num%2:
        return False
    for div in range(3, int(math.sqrt(num))+1, 2):
        if not num%div:
            return False
    return True

@njit(fastmath=True)
def run_program(N):
    for i in range(N):
        res = is_prime(i)
        print(i - res)

if __name__ == '__main__':
    N = 1000000
    start = perf_counter()
    run_program(N)
    end = perf_counter()
    print(end - start)

