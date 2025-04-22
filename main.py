from addons.word_splitter import *
from addons.bit_operations import *
from algorithms.sos import *
from addons.gcd import *

# a * b mod n = 14 * 30 mod 11 = 2

s = 3  # words
w = 2  # word length
a = 14 # 1110
b = 30
n = 11 #11

r = 1 << (s*w)
a = (a*r)%n
b = (b*r)%n
n_prime = calc_n_prime_sos(n,s,w)

print("a = ",a)
print("b = ",b)
print("n_prime = ",n_prime)

print()

# n_prime ≡ -n⁻¹ mod W

n_prime=int_to_bit_words(n_prime,s,w)
n = int_to_bit_words(n,s,w)
a = int_to_bit_words(a,s,w)
b = int_to_bit_words(b,s,w)


result_mont = monpro_sos(a[:],b[:],n[:],n_prime[:],w)
print(result_mont)
print(monpro_sos(result_mont, [1,0,0], n, n_prime, w))

