def iterative_count_pair_numbers(numbers):
    pair_qtd_numbers = 0
    pair_numbers = list()
    for number in numbers:
        if number % 2 == 0:
            pair_qtd_numbers += 1
            pair_numbers.append(number)
    return pair_qtd_numbers, pair_numbers