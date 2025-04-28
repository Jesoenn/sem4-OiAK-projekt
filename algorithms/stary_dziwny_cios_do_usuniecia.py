from addons.bit_operations import *

def monpro_cios(a: list[int], b: list[int], n: list[int], n_prime: list[int], w: int):
    """
    :param a: mnożna w przestrzeni montgomery'ego
    :param b: mnożnik w przestrzeni montgomery'ego
    :param n: modulo, nieparzyste
    :param n_prime: -n^{-1} mod r
    :param w: dlugość 1 słowa w bitach
    :return: a*b * r^(-1) mod n
    """
    s = len(a)
    W = 1 << w
    t = [0] * (s + 2)

    for i in range(s):
        carry = 0
        for j in range(s):
            carry, sum_result = bin_add_num(t[j] + carry, a[j] * b[i], w)
            t[j] = sum_result
        t[s] = carry

        m = (t[0] * n_prime[0]) % W

        carry = 0
        for j in range(s):
            carry, sum_result = bin_add_num(t[j] + carry, m * n[j], w)
            t[j] = sum_result
        bin_add_arr(t, carry, s, w)

        t = t[1:] + [0]

    borrow = 0
    for i in range(s):
        borrow, diff = bin_sub_num(t[i], n[i], borrow, w)
    if borrow == 0:
        return t[:s]
    else:
        return t[:s]
