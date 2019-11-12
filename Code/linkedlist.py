#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        count = 0

        if self.is_empty():
            return 0

        node = self.head
        while node is not None:
            count += 1
            node = node.next

        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = Node(item)
        # TODO: Append node after tail, if it exists
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if self.tail is None:
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        test_node = Node(quality)
        node = self.head

        while node is not None:
            # TODO: Check if node's data satisfies given quality function
            if quality(node.data) == True:
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.length() == 0:
            raise ValueError('Item not found: {}'.format(item))

        if self.head.data is item:
            self.head = self.head.next
            if self.length() == 0:
                self.tail = None
            return

        prev_node = self.head
        curr_node = prev_node.next

        found = False
        while curr_node is not None:
            if curr_node.data == item:
                prev_node.next = curr_node.next
                found = True
                if self.head == prev_node:
                    self.head = prev_node
                if self.tail == curr_node:
                    self.tail = prev_node
            prev_node = curr_node
            curr_node = curr_node.next

        if found == False:
            raise ValueError('Item not found: {}'.format(item))

    def replace(self, old_item, new_item):
        if self.length() == 0:
            raise ValueError('Item not found: {}'.format(item))

        if self.head.data is old_item:
            self.head = self.head.next
            if self.length() == 0:
                self.tail = None
            return

        prev_node = self.head
        curr_node = prev_node.next

        found = False
        while curr_node is not None:
            if curr_node.data == old_item:
                curr_node.data = new_item
                found = True
                if self.head == prev_node:
                    self.head = prev_node
                if self.tail == curr_node:
                    self.tail = prev_node
            prev_node = curr_node
            curr_node = curr_node.next

        if found == False:
            raise ValueError('Item not found: {}'.format(old_item))



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))
    print(ll.find(lambda item: item == 'B'))
    ll.replace('B', 'A')
    print('list: {}'.format(ll))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()
