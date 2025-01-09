'''
Lesson 05 - Scope
scope
nonlocal
global
'''
s = 'initial global variable'

def variable_scope():
    def assign_local():
        s = 'local variable'
        print(f'Inside function (after assignment): {s}')

    def assign_nonlocal():
        nonlocal s
        print(f'Inside function (before assignment): {s}')
        s = 'nonlocal variable'
        print(f'Inside function (after assignment): {s}')

    def assign_global():
        global s
        print(f'Inside function (before assignment): {s}')
        s = 'global variable'
        print(f'Inside function (after assignment): {s}')

    s = 'initial variable'

    print('\nLocal scope')
    print(f'Before function: {s}')
    assign_local()
    print(f'After function: {s}')

    print('\nNonlocal scope')
    print(f'Before function: {s}')
    assign_nonlocal()
    print(f'After function: {s}')

    print('\nGlobal scope')
    print(f'Before function: {s}')
    assign_global()
    print(f'After function: {s}')

def main():
    variable_scope()

if __name__ == '__main__':
    main()