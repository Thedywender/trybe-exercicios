# def soma_recursive(n):
#     if n == 0:
#         return 0
#     else:
#         print(n)
#     return n + soma_recursive(n-1)

def division_recursive(qtd_problemas):
    if qtd_problemas == 0:
        return 0
    else:
        print(qtd_problemas)
    return division_recursive(qtd_problemas/2)

print(division_recursive(4))