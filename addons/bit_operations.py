def bin_add_num(a: int, b:int, word_bit_length: int) -> tuple[int, int]:
    """
    :return: carry, sum
    """
    max_value = (1<<word_bit_length)-1        # max value for w bits
    sum_result = a + b
    carry = 1 if sum_result > max_value else 0
    sum_result = sum_result & max_value       # cut to match max_value bits number
    return carry, sum_result

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
