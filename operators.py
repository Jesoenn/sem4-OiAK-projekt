def int_to_bit_words(number: int, s: int, w: int):
    """
    :param number: int number
    :param s: how many words
    :param w: word length
    :return: s words of w-bit long integers
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
    return words