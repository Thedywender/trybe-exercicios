def cria_triangulo(lado1, lado2, lado3):

    is_triangle = (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1)
    if not is_triangle:
        return "Não é um triagulo"
    elif lado1 == lado2 == lado3:
        return "equilátero"
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return "isósceles"
    else:
        return "escaleno" 
    
print(cria_triangulo(2, 2, 80))