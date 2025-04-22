from addons.word_splitter import *

# r * r^-1 - n * n' = 1
def extended_euclidean(r: int, n: int) -> tuple[int, int]:
    if n == 0:
        return 1, 0
    else:
        x1, y1 = extended_euclidean(n, r % n)
        r_inv, n_prime = y1, x1 - (r // n) * y1
        print()
        print(r_inv, n_prime)
        print()
        return r_inv, n_prime


def calc_n_prime_sos(n: int, words, bits_in_word) -> int:
    """
    :param n: modulo calego algorytmu, liczba nieparzysta
    :param words: (s) słowa
    :param bits_in_word: (w) bity w słowie
    :return: (n') n_prime
    """
    if n % 2 == 0:
        raise ValueError("n musi być nieparzyste")
    r = 1 << (words * bits_in_word)             # r = 2^(s * w)
    r_inv, n_prime = extended_euclidean(r, n)   # extended Euclidean algorithm
    n_prime = n_prime%r                       # n > 0
    return n_prime