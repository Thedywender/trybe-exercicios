from array_example import ListaArray


class Matrix(ListaArray):

    def get(self, row, column):
        return self.data[row][column]

    def set(self, row, column, value):
        """Caso a linha não exista, uma nova linha
        será criada."""
        try:
            self.data[row].insert(column, value)
        except IndexError:
            self.data.insert(row, [value])

    def remove(self, row, column):
        # removeremos o item, retornando-o
        return self.data[row].pop(column)

print('----- Arrays multidimensionais')
array = Matrix()
array.set(0, 0, "Marcos")
print(array)
array.set(0, 0, 6)
print(array)
array.set(0, 2, 9)

array.set(1, 0, "Patrícia")
print(array)
array.set(1, 1, 9)
print(array)
array.set(1, 2, 6)

print(array)

# remove o índice 2, da primeira linha com o valor 9
array.remove(0, 1)
array.remove(1, 2)


print(array)
