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

        carry, sum_result = bin_add_num(t[s],carry, w)
        t[s] = sum_result
        t[s+1] = carry
        carry = 0


        m = (t[0] * n_prime[0]) % W

        # Ulepszona wersja z pdf

        carry, sum_result = bin_add_num(t[0], m*n[0], w)
        for j in range(1, s):
            carry, sum_result = bin_add_num(t[j] + carry, m*n[j],w)
            t[j-1] = sum_result     # t[j] -> t[j-1]

        carry, sum_result = bin_add_num(t[s], carry,w)
        t[s-1] = sum_result
        t[s] = t[s+1] + carry
        # Stara wersja
        # for j in range(s):
        #     carry, sum_result = bin_add_num(t[j] + carry, m * n[j], w)
        #     t[j] = sum_result

        # carry,sum_result = bin_add_num(t[s], carry, w)
        # t[s] = sum_result
        # t[s+1] = t[s+1]+carry

        # for j in range (s+1):     # to tez do usunięcia
        #     t[j]=t[j+1]


    u = t[:s+1]
    # Obojętnie który albo ten albo wyżej
    # u = [0] * (s + 1)  # u length = s+1
    # for i in range(s + 1):
    #     u[i] = t[i]

    borrow = 0
    for i in range(s):
        borrow, difference = bin_sub_num(u[i], n[i], borrow, w)
        t[i] = difference
    borrow, difference = bin_sub_num(u[s], 0, borrow, w)
    t[s] = difference

    if borrow == 0:
        return t[:s]  # t < n
    else:
        return u[:s]  # t >= n
