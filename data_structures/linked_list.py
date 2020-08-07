class Node:
    """ The linked list contains a series of connected nodes. Each node holds data. """

    def __init__(self, data):
        """ Constructor for Node class

        :param data: any data that the node will hold
        """
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other):
        return self.data == other.data


class LinkedList:
    """ Object representation of a linked list (a mutable container type)."""

    def __init__(self):
        """ List constructor. Sets list head and tail to None."""
        self.head = None
        self.tail = None

    def insert_head(self, data):
        """ Insert a Node at the head of the list. Big(O) = 1

        :param data: data to be stored in new node at head
        :return: None
        """
        new_node = Node(data)  # create a new node
        if self.head:  # if list is not empty
            new_node.next = self.head  # link new_node to head
        else:
            self.tail = new_node
        self.head = new_node  # make NewNode as head

    def insert_tail(self, data) -> None:
        """ Insert a Node at the tail of the list. Big(O) = n

        :param data: data to be stored in new node at head
        :return: None
        """
        if self.head is None:
            self.insert_head(data)  # if this is first node, call insert_head
        else:
            temp = self.head
            while temp.next:  # traverse to last node
                temp = temp.next
            # create node & link to tail
            new_node = Node(data)
            temp.next = new_node
            self.tail = new_node

    def insert_at(self, data, position):
        """ Insert a node at position in the linked list. Big(O) = n

        :param data: data to be stored in new node at position
        :param position: position for new node to be located after insertion
        :type position: int
        :return: None
        """
        if position == 0:
            self.insert_head(data)
        elif position < 0:
            raise IndexError("Index out of range.")
        else:
            previous = None
            current = self.head
            for i in range(position):
                previous = current
                current = current.next
                if current is None and i < position - 1:
                    raise IndexError("Index out of range.")

            temp = Node(data)
            previous.next = temp
            temp.next = current
            if current is None:
                self.tail = temp

    def delete_head(self):
        """ delete the node located at the head of the list. Big O = 1

        :return: deleted node
        :rtype: Node
        """
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None
        return temp

    def delete_tail(self):
        """ delete the node located at the tail of the list. Big O = n

        :return: deleted node
        :rtype: Node
        """
        temp = self.head
        if self.head:
            if self.head.next is None:
                # list only has one node
                self.head = None
            else:
                # find the second to last node
                while temp.next.next:
                    temp = temp.next
                # reassign tail
                self.tail = temp
                # move second to last pointer and delete last in one line
                temp.next, temp = None, temp.next
        return temp

    def __delitem__(self, position):
        """ delete a node from the list at a position. Big O = n

        :param position: index of the node to be deleted
        :return: None
        """
        if position == 0:
            self.delete_head()
        elif position < 0:
            raise IndexError("Index out of range.")
        else:
            previous = None
            current = self.head
            for i in range(position):
                previous = current
                current = current.next
                if current is None and i < position - 1:
                    raise IndexError("Index out of range.")
            previous.next = current.next
            if previous.next is None:
                self.tail = previous

    @property
    def is_empty(self):
        """ Boolean method. Big O = 1

        :return: True if list is empty, False if list has nodes in it
        :rtype: bool
        """
        return self.head is None  # return True if head is none

    def __reversed__(self):
        """ called by reversed() method to reverse the linked list. Big O = n

        :return: None
        """
        self.tail = self.head
        prev = None
        current = self.head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev

    def __repr__(self):
        """ string representation of linked list. Big O = n

        :rtype: str
        """
        current = self.head
        string_repr = ""
        while current:
            string_repr += str(current)
            if current is self.head:
                string_repr += '[HEAD]'
            if current is self.tail:
                string_repr += '[TAIL]'
            string_repr += ' --> '
            current = current.next
        # END represents end of the LinkedList
        return string_repr + "None"

    def __getitem__(self, index):
        """ get Node at index. Big O = n

        :param index: index at which to retrieve mode
        :return: Node at index
        :rtype: Node
        """
        current = self.head

        # If LinkedList is empty
        if current is None:
            raise IndexError("The Linked List is empty")

        # Move Forward 'index' times
        for i in range(index):
            # If the LinkedList ends before reaching specified node
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        return current

    def __setitem__(self, index, data):
        """ set data of Node at index to data. Big O = n

        :param index: index to modify data at
        :param data: new data for Node
        :return: None
        """
        current = self.head
        # If list is empty
        if current is None:
            raise IndexError("The Linked List is empty")
        for i in range(index):
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        current.data = data

    def __len__(self):
        """
        Return length of linked list (number of nodes). Big O = n

        :return: length of list
        :rtype: int
        """
        if not self.head:
            return 0

        count = 0
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count + 1

    def __contains__(self, item):
        """ Boolean method to determine if item is contained in list. Big O = n

        :param item: item to search for in data of all nodes
        :return: True if item is in list, False if item is not in list
        :rtype: bool
        """
        return any(elem == Node(item) for elem in self)


if __name__ == "__main__":
    a = LinkedList()
    print(a)
    a.insert_head(1)
    print(a)
    a.insert_tail(2)
    print(a)
    a.insert_at(1.5, 1)
    print(a)
    a.insert_at(3, 3)
    print(a)
    a.insert_at(0, 0)
    print(a)
    try:
        a.insert_at(6, 6)
    except IndexError:
        print('caught')
    print(a)
    a.delete_head()
    print(a)
    a.delete_tail()
    print(a)
    a.__delitem__(2)
    print(a)
    a.__delitem__(1)
    print(a)
    a.__delitem__(0)
    print(a)
    a.delete_head()
    print(a)
    a.delete_tail()
    print(a)

    a.insert_head(0)
    a.insert_at(1, 1)
    a.insert_at(2, 2)
    a.insert_at(3, 3)
    print(a)
    a_rev = reversed(a)
    print(a)
    for element in a:
        print(element)

    print(a.__contains__(2))
    print(a.__contains__(-1))
