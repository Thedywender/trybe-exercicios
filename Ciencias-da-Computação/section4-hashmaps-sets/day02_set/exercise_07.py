class Conjunto:
    def __init__(self) -> None:
        self.set = [False] * 1001
        self.last_element = 0

    def add(self, item):
        if not self.set[item]:
            self.set[item] = True
        if item > self.last_element:
            self.last_element = item

    def __contains__(self, item):
        return self.set[item]

    def union(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.set[index] or conjunto_b.set[index]:
                new_conjunto.add(index)

        return new_conjunto

    def intersection(self, conjunto_b):
        new_intersection = Conjunto()

        for index in range(1001):
            if self.set[index] and conjunto_b.set[index]:
                new_intersection.add(index)

        return new_intersection

    def difference(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.set[index] and not conjunto_b.set[index]:
                new_conjunto.add(index)

        return new_conjunto

    def issubset(self, conjunto_b):
        for index in range(1001):
            if self.set[index] and not conjunto_b:
                return False
        return True

    def issuperset(self, conjunto_b):
        for index in range(1001):
            if conjunto_b.set[index] and not self.set[index]:
                return False

        return True

    # def __str__(self):
    #     return str([i for i, x in enumerate(self.set) if x])  # Adicionado este método

    def __str__(self):
        string = "{"

        for index, is_in_set in enumerate(self.set):
            if is_in_set:
                string += str(index)
                if index < self.last_element:
                    string += ", "

        string += "}"
        return string


if __name__ == "__main__":
    estudantes = Conjunto()
    for i in range(1, 8):
        estudantes.add(i)

    lista1_entregue = Conjunto()
    for i in [1, 4, 7, 3]:
        lista1_entregue.add(i)

    lista2_entregue = Conjunto()
    for i in [3, 1, 6]:
        lista2_entregue.add(i)

    not_list_01 = estudantes.difference(lista1_entregue)

    entregou_todas_listas = estudantes.intersection(lista1_entregue).intersection(
        lista2_entregue
    )

    entregou_qualquer_lista = lista1_entregue.union(lista2_entregue)

    nao_entregou_listas = estudantes.difference(entregou_qualquer_lista)

print(not_list_01)
print(entregou_todas_listas)
print(entregou_qualquer_lista)
print(nao_entregou_listas)
