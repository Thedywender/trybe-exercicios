def selection_sort(array):
    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]

    return array

print(selection_sort([5, 9, 3, 1, 2, 8, 4, 7, 6, 0]))