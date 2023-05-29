class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        def my_stack(node_):
            if node_:
                if node_.next_node:
                    return node_.data + '\n' + my_stack(node_.next_node)
                return node_.data

        return my_stack(self.top)

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if not self.top:
            return None
        data = self.top.data
        if self.top.next_node:
            self.top = self.top.next_node
        else:
            self.top = None
        return data
