#!/usr/bin/python3
"""Singly linked list and node module"""


class Node:
    """Class representing a node in a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes a node with data and a reference to the next node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data stored in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data stored in the node"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Getter for the reference to the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the reference to the next node"""
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Class representing a singly linked list"""
    def __init__(self):
        """Initializes an empty singly linked list"""
        self.head = None

    def __str__(self):
        """Generates a string representation of the linked list"""
        ret = ""
        node = self.head
        while node:
            ret += str(node.data) + "\n"
            node = node.next_node
        return ret[:-1]

    def sorted_insert(self, value):
        """Inserts a node with a value into the sorted linked list"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        if node.next_node:
            new_node.next_node = node.next_node
        node.next_node = new_node
