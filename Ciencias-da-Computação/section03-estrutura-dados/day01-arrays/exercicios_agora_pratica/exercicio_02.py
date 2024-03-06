
def shuffle(items):
    answer = []
    div_cards_by_two = len(items) // 2
    for offset in range(div_cards_by_two):
        answer.extend(items[offset::div_cards_by_two])
    return answer

# Exemplo 1:
cartas = [2, 6, 4, 5, 9, 3, 8, 10]
# cartas por parte = 2
print(shuffle(cartas))

resultado = [2, 4, 6, 5]

# Exemplo 2:
cartas1 = [1, 4, 4, 7, 6, 6]
# cartas1 por parte = 3
print(shuffle(cartas1))

resultado = [1, 7, 4, 6, 4, 6]