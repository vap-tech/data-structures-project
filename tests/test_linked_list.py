"""Здесь тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        ll = LinkedList()
        ll.insert_beginning({'num': 2})
        ll.insert_at_end({'num': 3})
        ll.insert_at_end({'num': 4})
        ll.insert_beginning({'num': 1})
        self.assertEqual(str(ll), "{'num': 1} -> {'num': 2} -> {'num': 3} -> {'num': 4} -> None")

        ll2 = LinkedList()
        self.assertEqual(str(ll2), "None")
        ll2.insert_at_end({'one': 1})
        self.assertEqual(str(ll2), "{'one': 1} -> None")
