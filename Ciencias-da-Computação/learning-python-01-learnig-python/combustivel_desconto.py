def combustivel_desconto(litros, tipo_combustivel):
    if tipo_combustivel == "A":
        preco = 1.90
        desconto = 0.03
        if litros <= 20:
            desconto = 0.05

    elif tipo_combustivel == "G":
        preco = 2.50
        desconto = 0.04
        if 1 <= litros <= 20:
            desconto = 0.06

    total_preco = litros * preco
    total_preco -= total_preco * desconto
    return total_preco


print(combustivel_desconto(20, "A"))