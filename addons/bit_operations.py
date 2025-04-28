def bin_add_num(a: int, b:int, word_bit_length: int) -> tuple[int, int]:
    """
    Przeniesienie może wynieść więcej niż 1, więc musi być tak(w sos jako argument a jest dane równanie!)
    :return: carry, sum
    """
    max_value = (1 << word_bit_length) - 1
    total_sum = a+b
    carry = total_sum >> word_bit_length    # move right by word. Oldest bits as int are carry
    result = total_sum & max_value
    return carry, result



def bin_add_arr(array: list[int], carry:int, index: int, word_bit_length: int):
    """
    Dodaje przeniesienie (carry) do tablicy słów od zadanego indeksu.
    :param array: lista słów od najmniej do najbardziej znaczącego
    :param carry: przeniesienie
    :param index: od ktorego indeksu dodawanie
    :param word_bit_length: dlugosc slowa w bitach
    """

    while carry > 0 and index < len(array):
        carry, sum_result = bin_add_num(array[index], carry, word_bit_length)
        array[index] = sum_result
        index += 1
    return

def bin_sub_num(a: int, b: int, borrow: int, word_bit_length: int) -> tuple[int, int]:
    """
    a - b - borrow
    :return: new borrow, result
    """
    result = a - b - borrow
    if result < 0:
        result += (1 << word_bit_length)
        return 1, result  # borrow occurred
    else:
        return 0, result
