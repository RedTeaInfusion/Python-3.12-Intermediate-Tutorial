'''
Lesson 03 - Mutable and immutable
mutable
immutable
hashable
unhashable
id()
hash()
'''
def mutability():
    mutable = [1, 2, 3]
    print(f'Initial list: {mutable}, ID: {id(mutable)}')

    def modify_list(l):
        print(f'Inside function (before modification): {l},\tID: {id(l)}')
        l.append(4)
        print(f'Inside function (after modification): {l},\tID: {id(l)}')

    modify_list(mutable)
    print(f'Final list: {mutable}, ID: {id(mutable)}')

    return mutable

def immutability():
    immutable = 'hello'
    print(f'Initial string: {immutable}, ID: {id(immutable)}')

    def modify_string(s):
        print(f'Inside function (before modification): {s},\tID: {id(s)}')
        s += ' world'
        print(f'Inside function (after modification): {s},\tID: {id(s)}')
        return s
    
    modify_string(immutable)
    print(f'Final string (unchanged): {immutable}, ID: {id(immutable)}')

    immutable = modify_string(immutable)
    print(f'Final string (changed): {immutable}, ID: {id(immutable)}')
    
    return immutable

def hashability(lst, s):
    print(hash(s))

    try:
        print(hash(lst))
    except TypeError as e:
        print(e)

def main():
    lst = mutability()
    s = immutability()
    hashability(lst, s)

if __name__ == '__main__':
    main()