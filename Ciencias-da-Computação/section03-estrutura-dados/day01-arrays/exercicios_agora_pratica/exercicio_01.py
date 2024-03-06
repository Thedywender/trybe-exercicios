# 1 - OK
# 0 - Instabilidades

def verificar_instabilidades(valores_coletados):
    # escreva o seu código aqui
    estabilidade = 0
    tempo_max = 0
    for i in range(len(valores_coletados) - 1):
        if valores_coletados[i] == 1:
            estabilidade += 1
            if valores_coletados[i] == 0:
                estabilidade = 0
        if estabilidade > tempo_max:
            tempo_max = estabilidade
    return tempo_max


valores_coletados = [0, 1, 1, 1, 0, 0, 1, 1]
resultado = 3

# valores_coletados = [1, 1, 1, 1, 0, 0, 1, 1]
# resultado = 4

print(verificar_instabilidades(valores_coletados))

# Resposta da análise de complexidade

# O algoritmo realiza um for, portanto possui Complexidade de Tempo O(n).