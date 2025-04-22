def int_to_bit_words(number: int, s: int, w: int):
    """
    ERROR jak da się ujemne liczby
    :param number: liczba całkowita int
    :param s: liczba słów
    :param w: długość słowa w bitach
    :return: s słów o w-bitowych liczbach od najmłodszego słowa do najstarszego
    """
    # binary without prefix '0b'
    binary_representation = bin(number)[2:].zfill(s * w)    # fill with zeros
    words = []                                              # words list
    #print(binary_representation)

    # divide binary to multiple words of length w
    for i in range(0, len(binary_representation), w):
        word = binary_representation[i:i + w]               # from index i to i+w
        #print(word)
        words.append(int(word, 2))

    #print(words)
    return reverse_words(words) # reverse list -> youngest words to oldest (needed for SOS)


def reverse_words(words: list[int]):
    """
    :param words: słowa od najstarszych do najmłodszych
    :return: słowa od najmłodszych do najstarszych
    """
    new_words = []
    for i in range(len(words) - 1, -1, -1):
        new_words.append(words[i])
    return new_words