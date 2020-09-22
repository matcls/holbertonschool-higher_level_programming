#!/usr/bin/python3
"""defines a node of a singly linked list"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a Node

        args:
            data (int): Node data.
            next_node (Node): next Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve Node data.

         Returns:
            int: Node data
         """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the Node data.

            Args:
                value (int): Node data.

            Returns:
                int: Node data.
            """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrive next_node value.

        Returns:
            Node: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets next_node value.

            Returns:
                Node: next_node
            """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a SinglyLinkedList"""

    def __init__(self):
        """Initialize a SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Prints a SinglyLinkedList."""
        string = ""
        h = self.__head
        while h:
            string += str(h.data)
            string += '\n'
            h = h.next_node
        string = string[:-1]
        return string

    def sorted_insert(self, value):
        """Inserts a new Node in a SinglyLinkedList.

        the correct sorted position in the list (increasing order).

        Args:
            value (Node): Value of the ne Node
        """
        h = self.__head
        new = Node(value)
        if h is None:
            self.__head = Node(value)
        elif h.data >= new.data:
            new.next_node = h
            self.__head = new
        else:
            while h.next_node:
                if h.next_node.data >= new.data:
                    new.next_node = h.next_node
                    h.next_node = new
                    break
                else:
                    h = h.next_node
            if h.next_node is None:
                h.next_node = new
