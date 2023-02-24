import time
import tornado


def f(g, k):
    return g + k


if __name__ == "__main__":
    g = 123
    k = 281
    print(g, k)
    result = f(g, k)
    print('result', result)
    my_str = 'n23n1k2'
    my_str.upper()

    my_l = [1, 41, 61, 99, 'some string']
