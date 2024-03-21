# def imprime_inverse(name):
#     modify_name = ''
#     len_name = len(name)
#     for letter in name:
#         len_name -= 1
#         modify_name += letter

# imprime o nome desestruturado letra por letra
# def vertical_inverted_ladder(word):
#     add_num = 0
#     for index in range(len(word) - add_num):
#         add_num += 1
#         print(word[index])
#     print()


# def vertical_inverte_latter(word):
#     for removed_letters in range(len(word)):
#         for index in range(len(word) - removed_letters):
#             print(word[index], end="")
#         print()


# menor complexidade
def vertical_inverted_ladder(word):
    for i in range(len(word), 0, -1):
        print(word[:i])


if __name__ == "__main__":
    name = input("Digite um nome: ")
    vertical_inverted_ladder(name)
