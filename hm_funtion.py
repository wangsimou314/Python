def multiple_table():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print('%d * %d = %d' % (j, i, j * i), end='\t')
            j += 1
        print('')
        i += 1


def sum(a, b):
    """这是个注释"""
    c = a + b
    return c


def print_line(char, times, l):
    i = 1
    while i <= l:
        print(char * times)
        i += 1
