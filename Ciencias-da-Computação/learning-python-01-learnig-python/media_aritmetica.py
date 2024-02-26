def media_aritmetica(numbers):
    sum_media = sum(numbers)
    media = sum_media / len(numbers)
    return int(media)


numbers = [3, 4, 5, 6, 7, 8, 9]

print(media_aritmetica(numbers))
