# s - liczba słów
# C przeniesienie, S suma
#
from addons.bit_operations import *


def monpro_sos(a: list[int], b: list[int], n: list[int], n_prime: list[int], w: int):
    """
    :param a: mnożna w przestrzeni montgomery'ego
    :param b: mnożnik w przestrzeni montgomery'ego
    :param n: modulo, nieparzyste
    :param n_prime: -n^{-1} mod r
    :param w: dlugość 1 słowa w bitach
    :return: a*b = u * r^-1 mod n
    """
    s = len(a)  # words number
    W = 1 << w  # move 1 to the left (w bits) -> max word number
    t = [0]*(2*s+1)  # 2s+1 words
    r = s*w # shift by s*w bits

    # Step 1 -> a * b | little-endian -> a[0]: least significant, a[max]: most significant !!
    # Example: s,w=2 | a = 7(10) = 01 11 (big-endian) = 11 01 (little-endian)
    for i in range(s):
        carry = 0
        for j in range(s):
            carry,sum_result = bin_add_num(t[i+j]+carry,a[j]*b[i],w)
            t[i+j]=sum_result
        t[i+s] = carry

    # Step 2 -> t + m * n
    for i in range(s):
        carry = 0
        m = t[i]*n_prime[0]%W
        for j in range(s):
            carry, sum_result = bin_add_num(t[i + j] + carry, m*n[j], w)
            t[i + j] = sum_result
        bin_add_arr(t,carry,i+s,w)           # add with carry from t[i+s]

    # Step 2.5 -> create u -> (t+m*n)/r
    u = [0]*(s+1)       # u length = s+1
    for i in range(s):
        u[i] = t[i+s]

    # Step 3 -> u - n (word by word)
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


#
# #testy
#
# a = [3,1] # 7
# b = [2, 0] # 2
# s = 2
# w = 2
# t = [0]*(2*s+1)  # 2s+1 words
#
#
# print(t)