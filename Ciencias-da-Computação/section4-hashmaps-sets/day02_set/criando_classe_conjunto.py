class Conjunto:
    def __init__(self) -> None:
        self.set = [False] * 1001
        self.last_element = 0

    def add(self, item):
        if not self.set[item]:
            self.set[item] = True
        if item > self.last_element:
            self.last_element = item

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

    def __contains__(self, item):
        return self.set[item]

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
    conj = Conjunto()

    # array = [0, 10, 100, 1000]
    # for i in array:
    #     conj.add(i)
    # print(conj)

    # conj2 = Conjunto()
    # for i in [1, 2, 3]:
    #     conj2.add(i)
    # print(conj2)

    # conj3 = Conjunto()
    # for i in [7, 2, 10]:
    #     conj3.add(i)
    # print(conj3)

    # conj4 = Conjunto()
    # print(conj4)

# for i in [1, 2, 3]:
#     conj.add(i)
# print(conj)
# print(1 in conj)
# print(0 in conj)


conj1 = Conjunto()
for i in range(1, 17):
    conj1.add(i)

conj2 = Conjunto()
for i in range(10, 21):
    conj2.add(i)

conj3 = conj1.intersection(conj2)
print(conj3)
