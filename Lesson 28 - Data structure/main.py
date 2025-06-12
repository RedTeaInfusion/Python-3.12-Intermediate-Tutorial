'''
Lesson 28 - Data structure
bytes
bytearray
stack LIFO
queue FIFO
linked list
'''
from queue import Queue

def demo_bytes():
    print('\n=== Bytes ===')
    b1 = bytes([72, 101, 108, 108, 111])
    print(type(b1), b1)
    print(b1[0])
    print(b1.find(b'o'))
    b2 = b'Hello World'
    print(type(b2), b2)
    s1 = 'Python'
    b3 = bytes(s1, 'utf-8')
    print(type(b3), b3)

def demo_bytearray():
    print('\n=== Bytearray ===')
    b = bytearray([72, 101, 108, 108, 111])
    print(type(b), b)
    b[0] = 74
    print(b)
    b.append(33)
    print(b)
    b.pop()
    print(b)
    b.extend(b)
    print(b)


def demo_stack():
    print('\n=== Stack ===')
    stack = []
    stack.append('a')
    print(type(stack), stack)
    stack.append('b')
    stack.append('c')
    print(stack)
    stack.pop()
    print(stack)

def demo_queue():
    print('\n=== Queue ===')
    q = Queue()
    print(type(q), q.queue)
    q.put('1')
    print(q.queue)
    q.put('2')
    print(q.queue)
    q.put('3')
    print(q.queue)
    q.get()
    print(q.queue)
    q.get()
    print(q.queue)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def demo_linked_list():
    print('\n=== Linked List ===')
    l = LinkedList()
    n1 = Node(1)
    l.head = n1
    print(l.head, l.head.next)
    n2 = Node(2)
    n3 = Node(3)
    l.head.next = n2
    n2.next = n3
    print(n1, n1.next)
    print(n2, n2.next)
    print(n3, n3.next)

    current = n1
    while current:
        print(current.data, end=' -> ')
        current = current.next
    else:
        print(current)

def main():
    demo_bytes()
    demo_bytearray()
    demo_stack()
    demo_queue()
    demo_linked_list()

if __name__ == "__main__":
    main()