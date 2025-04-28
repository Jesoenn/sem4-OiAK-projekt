from addons.word_splitter import *
from addons.bit_operations import *
from algorithms.sos import *
from addons.gcd import *

# SPRAWDZENIE
def montgomery_reduction(a, b, n, r, n_prime):
    t = a * b
    m = (t % r) * n_prime % r
    u = (t + m * n) // r
    if u >= n:
        u -= n
    return u

s = 3  # words
w = 3  # word length
a = 142  # 1110
b = 303
n=411

r = 1 << (s * w)
mont_a = (a * r) % n
mont_b = (b * r) % n
n_prime = calc_n_prime_sos(n, s, w)

print("mont_a = ", mont_a)
print("mont_b = ", mont_b)
print("n_prime = ", n_prime)


n_prime = int_to_bit_words(n_prime, s, w)
n = int_to_bit_words(n, s, w)
mont_a = int_to_bit_words(mont_a, s, w)
mont_b = int_to_bit_words(mont_b, s, w)


result_mont = monpro_sos(mont_a, mont_b, n, n_prime, w)  # in montgomery space
final_result = monpro_sos(result_mont, [1, 0, 0], n, n_prime, w)  # multiply by 1, to get normal number
print("final_result = ", final_result)
print("poprawny = ",int_to_bit_words((a * b) % 411, s, w))
print()
print("Oczekiwany wynik:", (a * b) % 411)
print("Wynik:           ", bit_words_to_int(final_result, w))
# if bit_words_to_int(final_result, w) == expected_number:
#     print("GIT")
# else:
#     print("ŹLE")
cos = montgomery_reduction(426,400,509,512,171)

