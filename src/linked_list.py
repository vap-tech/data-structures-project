class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            return
        node = Node(data)
        node.next_node = self.head
        self.head = node

    def insert_at_end(self, data) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
            return
        node = Node(data)
        self.tail.next_node = node
        self.tail = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self) -> list:
        """Возвращает список с данными, содержащимися в односвязном списке"""
        node = self.head
        data = []
        while node:
            data.append(node.data)
            node = node.next_node
        return data

    def get_data_by_id(self, data_id):
        """Возвращает первый найденный в `LinkedList` словарь с ключом 'id'"""
        node = self.head
        while node:
            data = None
            try:
                data = node.data['id']
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
            except KeyError:
                print('Данные не являются словарем или в словаре нет id.')
            if data == data_id:
                return node.data
            node = node.next_node
