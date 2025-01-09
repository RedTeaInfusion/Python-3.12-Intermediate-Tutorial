'''
Lesson 04 - Generator
generator
yield
'''
import sys

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    for n in fibonacci_sequence(10):
        print(n)

    for n in fibonacci_generator(10):
        print(n)

    print(sys.getsizeof(fibonacci_sequence(100)))
    print(sys.getsizeof(fibonacci_sequence(1000)))
    print(sys.getsizeof(fibonacci_generator(100)))
    print(sys.getsizeof(fibonacci_generator(100000000)))

if __name__ == '__main__':
    main()