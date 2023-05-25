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


if __name__ == '__main__':
    unittest.main()
