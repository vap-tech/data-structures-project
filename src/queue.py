class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        nd = Node(data, None)
        if not self.head:
            self.head = nd
            self.tail = nd
            return
        self.tail.next_node = nd
        self.tail = nd

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head:
            data = self.head.data
            if self.head.next_node:
                self.head = self.head.next_node
            else:
                self.head = None
                self.tail = None
            return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.head:
            return ''

        def my_func(node):
            if node:
                if node.next_node:
                    return node.data + '\n' + my_func(node.next_node)
                return node.data
        return my_func(self.head)
