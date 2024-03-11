def solucao(numbers, alvo):
    if len(numbers) == 0:
        return False
    for i in range(len(numbers) - 1):
        element = numbers[i]
        new_index = i + 1
        new_numbers = numbers[new_index:]
        if element + numbers[i + 1] == alvo:
            return True
        if new_index > len(numbers):
            return False
        solucao(new_numbers, alvo)
    return False