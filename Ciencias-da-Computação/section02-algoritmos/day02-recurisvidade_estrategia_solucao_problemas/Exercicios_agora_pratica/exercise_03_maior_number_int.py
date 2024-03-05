def biggest_number(numbers, tamanho):
    if tamanho == 1:
        return numbers[0]
    else:
        biggest = biggest_number(numbers, tamanho - 1)
        if numbers[tamanho - 1] > biggest:
            return numbers[tamanho - 1]
        else:
            return biggest
        
print(biggest_number([10, 20, 30, 40, 70, 60, 100], 7))