'''
Lesson 08 - PIP
pip
list
show
install and uninstall
numpy arange() add() where() reshape()
'''
import numpy as np
import time

def time_it(func):
    def func_with_timing(*args, **kwargs):
        start_time = time.time()
        print(start_time)
        result = func(*args, **kwargs)
        end_time = time.time()
        print(end_time)
        duration = end_time - start_time
        print(f"Function '{func.__name__}' executed in {duration:.8f} seconds")
        return result
    return func_with_timing

@time_it
def pure_python(size):
    a = list(range(size))
    b = list(range(size))
    c = [a[i] + b[i] for i in range(size)]
    return c

@time_it
def pure_numpy(size):
    a = np.arange(size)
    b = np.arange(size)
    c = np.add(a, b)
    return c

def main():
    array_len = 10**6
    n1 = pure_python(array_len)
    n2 = pure_numpy(array_len)
    print(
        f'{type(n1)} {type(n2)}\n'\
        f'{all(n1 == n2)}\n'\
        f'{n1[:10]}\n{n2[:10]}'
    )
    n2 = n2[n2 < 50]
    print(n2)
    n2 = np.where(n2 % 3 == 0, n2, 0)
    print(n2)
    n2 = np.reshape(n2, (5, 5))
    print(n2)
    print(n2.shape)
    print(np.square(n2))

if __name__ == '__main__':
    main()