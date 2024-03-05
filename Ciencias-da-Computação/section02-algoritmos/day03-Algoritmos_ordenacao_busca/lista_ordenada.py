def encontrar_menor_e_adicionar(lista):
    lista_ordenada = []  # Lista vazia para armazenar os elementos ordenados
    while lista:  # Enquanto houver elementos na lista original
        lista.sort()  # Ordena a lista em ordem alfabética
        menor_elemento = lista.pop(0)  # Remove e armazena o primeiro elemento (o menor)
        lista_ordenada.append(menor_elemento)  # Adiciona o menor elemento na nova lista
    return lista_ordenada

# Exemplo de uso:
minha_lista = ["banana", "abacaxi", "uva", "laranja", "maçã"]
nova_lista = encontrar_menor_e_adicionar(minha_lista)
print("Lista ordenada em ordem alfabética:", nova_lista)
