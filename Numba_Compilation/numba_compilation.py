from numba import njit
import time

n = 1000000


def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        a, b = a+b, a
    return a


start_1 = time.time()
fibonacci(n)
end_1 = time.time()
total_1 = end_1 - start_1


start_2 = time.time()
@njit(fastmath=True, cahce=True)
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        a, b = a+b, a
    return a
end_2 = time.time()
total_2 = end_2 - start_2

print("Время работы без ускорения: ", total_1, " ", "Время работы с ускорением: ",
      total_2, " ", "Разница во времения работы: ", total_1/total_2, " раз")
