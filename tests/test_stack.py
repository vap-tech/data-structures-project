"""Здесь тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_stack(self):
        # Пишем нужное количество проверок
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')  # data2
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')  # data1
        self.assertEqual(stack.top.next_node.next_node.next_node, None)  # None

        with self.assertRaises(AttributeError):
            print(stack.top.next_node.next_node.next_node.data)

        data = stack.pop()
        self.assertEqual(data, 'data3')
        self.assertEqual(stack.top.data, 'data2')
        stack.pop()
        self.assertEqual(stack.pop(), 'data1')
        self.assertEqual(stack.pop(), None)

    def test_stack3(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(str(stack), 'data3\ndata2\ndata1')
