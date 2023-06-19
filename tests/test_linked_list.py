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

    def test_get_data_by_id(self):
        llist = LinkedList()
        llist.insert_beginning({'id': 1, 'username': 'la508509'})
        llist.insert_at_end({'lsb': 'username'})
        llist.insert_at_end([1, 2, 3])
        llist.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEqual(llist.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})

    def test_to_list(self):
        llist2 = LinkedList()
        llist2.insert_beginning({'id': 1, 'username': 'l09'})
        lst = llist2.to_list()

        self.assertEqual(lst[0], {'id': 1, 'username': 'l09'})
