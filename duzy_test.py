from algorithms.cios import *
from algorithms.sos import *
from addons.gcd import *
from core.timer import *

# 7 BITÓW WSZYSTKO OK
# od 8 zaczynają być błędy


s = 2  # words
w = 200 # word length
a = 12313231 # 1110
b = 25311363

x = int(123456789012345678901234567890123456789012345678901234567890)
print(x)
input("STOP")

max_value = (1 << s*w) - 1          #maksymalne n dla w bitów
timer = Timer()

for i in range((1 << (s*w)-1)-1, max_value, 2):
    n = i
    n_int = n

    r = 1 << (s * w)
    mont_a = (a * r) % n
    mont_b = (b * r) % n
    n_prime = calc_n_prime_sos(n, s, w)

    # print("a = ", a)
    # print("b = ", b)
    # print("n_prime = ", n_prime)

    n_prime = int_to_bit_words(n_prime, s, w)
    n = int_to_bit_words(n, s, w)
    mont_a = int_to_bit_words(mont_a, s, w)
    mont_b = int_to_bit_words(mont_b, s, w)
    timer.start()
    result_mont = monpro_sos(mont_a, mont_b, n, n_prime, w)  # in montgomery space
    timer.stop()
    final_result = monpro_sos(result_mont, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], n, n_prime,w)  # multiply by 1, to get normal number

    # result_mont = monpro_cios(mont_a, mont_b, n, n_prime, w)  # in montgomery space
    # final_result = monpro_cios(result_mont, [1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0], n, n_prime, w)  # multiply by 1, to get normal number

    #print()
    expected_number = (a * b) % n_int
    received_number = bit_words_to_int(final_result, w)
    if received_number != expected_number:
        print("ŹLE")
        print("Testowane n:",i)
        print("Oczekiwany wynik:", (a * b) % n_int)
        print("Wynik:           ", received_number)
        input("Naciśnij Enter, aby kontynuować...")
    print("Testowane n:", i, "CZAS:",timer.time)