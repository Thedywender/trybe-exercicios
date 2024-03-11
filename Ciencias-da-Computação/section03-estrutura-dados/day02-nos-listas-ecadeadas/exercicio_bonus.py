from node import Node


class DoublyLinked:
    def __init__(self):
        self.head == None
        self.__length == 0
        self.tail == len(self) - 1

    def remove_first(self):
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

    def insert_last(
        self, value
    ):  # complexidade O(1) inserção de um item no final da lista
        if self.is_empty():
            return self.insert_first(value)

        new_last_value = Node(value)
        actual_last_value = self.__get_node_at(len(self) - 1)
        actual_last_value.next = new_last_value
        self.__length += 1

    def index_of_duplicate(self, value):  # complexidade O(n) percorre toda a lista
        position = 1
        current_value = self.head.next
        while current_value != self.tail:
            if current_value.value == value:
                return position
            current_value = current_value.next
            position += 1
        return -1

    def delete_duplicates(
        linked_list_content,
    ):  # complexidade O(n) percorre toda a lista
        list_with_unique_elements = DoublyLinked()

        while linked_list_content:
            value_removed = linked_list_content.remove_first()
            if list_with_unique_elements.index_of(value_removed.value) == -1:
                list_with_unique_elements.insert_last(value_removed)

        return list_with_unique_elements
