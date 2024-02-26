def maior_nome(nomes):
    maior = ""
    for nome in nomes:
        if len(nome) > len(maior):
            maior = nome
    return maior


nome_list = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
print(maior_nome(nome_list))
