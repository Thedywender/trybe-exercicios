class Estatistica:
    def __init__(self, numbers):
        self._numbers = numbers

    def media(self):
        return sum(self._numbers) / len(self._numbers)

    def mediana(self):
        lista_ordenada = sorted(self._numbers)
        n = len(self._numbers)
        if n % 2 == 0:
            return (lista_ordenada[n//2-1] + lista_ordenada[n//2]) / 2
        else:
            return self._numbers[n//2]

        def moda(self):
        number, _ = Counter(self.numbers).most_common()[0]
        return number

if __name__ == '__main__':


    estatistica = Estatistica([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    mediaResult = estatistica.media()
    medianaResult = estatistica.mediana()

    print(medianaResult)