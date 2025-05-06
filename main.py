from addons.word_splitter import *
from addons.bit_operations import *
from algorithms.sos import *
from addons.gcd import *
from algorithms.cios import *
import time

# a * b mod n = 14 * 30 mod 11 = 2
# testowane n: 61,11

s = 3  # words
w = 100  # word length
a = 999999999999999999999999999999 # 1110
b = 999999999999999999999999999999
n = 97
n_int=n

r = 1 << (s*w)
mont_a = (a*r)%n
mont_b = (b*r)%n
n_prime = calc_n_prime_sos(n,s,w)

print("a = ",a)
print("b = ",b)
print("n_prime = ",n_prime)

print()

n_prime=int_to_bit_words(n_prime,s,w)
n = int_to_bit_words(n,s,w)
mont_a = int_to_bit_words(mont_a,s,w)
mont_b = int_to_bit_words(mont_b,s,w)


start = time.perf_counter()
result_mont_sos = monpro_sos(mont_a,mont_b,n,n_prime,w)                # in montgomery space
final_result_sos =monpro_sos(result_mont_sos, [1,0,0], n, n_prime, w)    # multiply by 1, to get normal number
end = time.perf_counter()
print("Czas sos: ",(end - start)*1000, "ms")  # milisekundy



start = time.perf_counter()
result_mont = monpro_cios(mont_a,mont_b,n,n_prime,w)                # in montgomery space
final_result=monpro_cios(result_mont, [1,0,0], n, n_prime, w)    # multiply by 1, to get normal number
end = time.perf_counter()
print("Czas cios: ",(end - start)*1000, "ms")  # milisekundy




print("Oczekiwany wynik cios: ",(a*b)%n_int)
print("Wynik cios: ",bit_words_to_int(final_result,w))

print()


print("Oczekiwany wynik sos: ",(a*b)%n_int)
print("Wynik sos: ",bit_words_to_int(final_result_sos,w))
