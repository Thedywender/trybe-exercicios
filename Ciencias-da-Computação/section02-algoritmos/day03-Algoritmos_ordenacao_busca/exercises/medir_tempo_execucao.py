from time import perf_counter
import timeit


class Cronometro:
    def __init__(self, name="Seu algoritmo"):
        self.name = name
    def __enter__(self):
        self.start = perf_counter()
    def __exit__(self, *exc):
        elapsed = perf_counter() - self.start
        print(f"{self.name} demorou {elapsed} segundos")


inicio = timeit.default_timer()
Cronometro()
fim = timeit.default_timer()

print('Tempo de execução: ', fim - inicio)