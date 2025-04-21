# s - liczba słów
# C przeniesienie, S suma
#


def monpro_sos(a: list, b: list, n, n_prime, r, w: int):
    """
    :param a: mnożna
    :param b: mnożnik
    :param n: modulo, nieparzyste
    :param n_prime: -n^{-1} mod r
    :param r: 2^(s*w), gdzie s - liczba słów, w - wielkość słowa w bitach
    :param w:
    :return: a*b = u * r^-1 mod n
    """
    s = len(a)  # words number
    W = 1 << w  # move 1 to the left (w bits) -> max word number
    t = [0]*(2*s+1)  # 2s+1 words

    # Step 1
    for i in range(s):
        C = 0
        for j in range(s):
            product = t[i+j]+a[j]*b[i]+C
            t[i+j] = product%W  #S -> lower w-bits
            C = product//W      #carry -> all bits minus lower w-bits
        t[i+s] = C




    return t  # tymczasowo, tylko mnożenie


# POTESTOWAC BO a[0] jest najmniej znaczące

a = [1, 3] # 7 -> 01 11
b = [0, 2] # 2 -> 00 10
w = 2

s = len(a)  # words number
W = 1 << w  # move 1 to the left (w bits) -> max word number
t = [0]*(2*s+1)  # 2s+1 words

# Step 1
for i in range(s):
    C = 0
    for j in range(s):
        product = t[i+j]+a[j]*b[i]+C
        t[i+j] = product%W  #S -> lower w-bits
        C = product//W      #carry -> all bits minus lower w-bits
    t[i+s] = C

print(t)