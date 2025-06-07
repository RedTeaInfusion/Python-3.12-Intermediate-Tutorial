'''
Lesson 27 - Algorithm
time complexity
space complexity
O()
'''
def is_even(number):
    '''
    n = 1
    f(n) = 1
    O(1) TIME, O(1) SPACE
    '''
    return number % 2 == 0

def find_item(items, target):
    '''
    n = len(items)
    f(n) = n
    O(n) TIME, O(1) SPACE
    '''
    items.extend(items)
    for item in items:
        if item == target:
            return True
    return False

def find_item_2(items, target):
    '''
    n = len(items)
    f(n) = n
    O(n) TIME, O(n) SPACE
    '''
    visited = []
    for item in items:
        visited.append(item)
        if item == target:
            break
    return visited

def has_duplicates(items):
    '''
    n = len(items)
    n1 = n
    n2 = n/2
    f(n) = n1*n2 = (n^2)/2
    O(n^2) TIME, O(1) SPACE
    '''
    for i in range(len(items)):#n1
        for j in range(i + 1, len(items)):#n2
            if items[i] == items[j]:
                return True
    return False

def is_perfect_square(n):
    '''
    n = 1 = 1^2
    n = 4 = 2^2
    n = 9 = 3^2
    n = k^2
    sqrt(n) = k
    O(sqrt(n)) TIME, O(1) SPACE
    '''
    k = 1
    while k * k <= n:
        if k * k == n:
            return True
        k += 1
    return False

def is_power_of_two(n):
    '''
    n/2 = n/(2^1)
    n/4 = n/(2^2)
    n/8 = n/(2^3)
    n/2^k
    we stop when n/2^k = 1
    n = 2^k
    log(n) = log(2^k)
    log(n) = k
    O(log(n)) TIME, O(1) SPACE
    '''
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return n == 1
