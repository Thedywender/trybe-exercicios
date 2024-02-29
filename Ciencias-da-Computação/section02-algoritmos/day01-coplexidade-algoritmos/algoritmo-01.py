def sum_array(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum

print(sum_array([1, 2, 3, 4, 5])) # 15

def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
        array_of_squares.append(number * number)

    return array_of_squares

print(squared_array([1, 2, 3, 4, 5])) # [1, 4, 9, 16, 25]

def multiply_array(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result