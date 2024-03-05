def insertion_sort(array):
    for i in range(len(array)):

        current_position = i
        current_value = array[i]

        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            array[current_position], current_position = array[current_position - 1], current_position - 1

        array[current_position] = current_value

    return array

print(insertion_sort([5, 9, 3, 1, 2, 8, 4, 7, 6, 0]))