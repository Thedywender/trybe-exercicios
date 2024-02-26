def cobertura_tinta(metros_quadrados):
    litros = metros_quadrados / 3
    latas = litros / 18
    return litros, float(latas)

metros_quadrados = 100

litros, latas = cobertura_tinta(metros_quadrados)

print(f'Você precisará de {litros:.2f} litros de tinta e {latas:.2f} latas de tinta.')
