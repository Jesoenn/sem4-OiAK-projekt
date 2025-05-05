import argparse
import random
from addons.word_splitter import *
from algorithms.sos import *
from algorithms.cios import *
from addons.gcd import *
from core.timer import *

def run_simulation(args: argparse.Namespace):
    algorithm = args.algorithm
    w = args.bits
    s = args.words
    n = args.n
    n_int = args.n
    if args.n is None:
        n = random.getrandbits(w*s) | 1
        n_int = n
    a = args.a
    if a is None:
        a = random.randint(0, n - 1) # from 0 to n-1
    b = args.b
    if b is None:
        b = random.randint(0, n - 1)

    file_name = args.file

    timer = Timer()
    # simulation
    timer.start()
    r = 1 << (s * w)

    # starting calculations
    mont_a = (a * r) % n
    mont_b = (b * r) % n
    n_prime = calc_n_prime_sos(n, s, w)

    # convert to bit words (list)
    n_prime = int_to_bit_words(n_prime, s, w)
    n = int_to_bit_words(n, s, w)
    mont_a = int_to_bit_words(mont_a, s, w)
    mont_b = int_to_bit_words(mont_b, s, w)
    final_result = -1
    if algorithm == 0: # SOS
        result_mont = monpro_sos(mont_a, mont_b, n, n_prime, w)
        timer.stop()
        # back to normal space -> result_mont*1
        final_result = monpro_sos(result_mont, int_to_bit_words(1, s, w), n, n_prime,w)

    if algorithm == 1: # CIOS
        result_mont = monpro_cios(mont_a, mont_b, n, n_prime, w)
        timer.stop()
        # back to normal space -> result_mont*1
        final_result = monpro_cios(result_mont, int_to_bit_words(1, s, w), n, n_prime, w)

    expected_number = (a * b) % n_int
    received_number = bit_words_to_int(final_result, w)
    print("Result:",received_number)
    print("Expected result:",expected_number)
    print("Is result correct: ",expected_number==received_number)
    print("Time:",timer.time)

    if fileName:
        total_bits = w * s
        alg_name = "SOS" if algorithm == 0 else "CIOS"
        formatted_time = str(timer.time).replace('.', ',')
        # Algorithm Bits Words TotalBits Time[ms] Correct(Y/N)
        with open(fileName, "a") as f:
            f.write(f"{alg_name}\t{s}\t{w}\t{total_bits}\t{formatted_time}\t{expected_number == received_number}\n")
