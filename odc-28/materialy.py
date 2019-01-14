import time


def find_fib_num_rec(num):
    if num == 1 or num == 2:
        return 1
    else:
        return find_fib_num_rec(num - 2) + find_fib_num_rec(num - 1)


def find_fib_num_loop(num):
    a, b = 0, 1
    for elem in range(num):
        a, b = b, a + b
    return a


start = time.process_time()
print(find_fib_num_rec(36))
stop = time.process_time()
print(f'Czas wykonywania funkcji "find_fib_num_rec" wynosi: {stop-start}')

start1 = time.process_time()
print(find_fib_num_loop(36))
stop1 = time.process_time()
print(f'Czas wykonywania funkcji "find_fib_num_loop" wynosi: {stop1-start1}')