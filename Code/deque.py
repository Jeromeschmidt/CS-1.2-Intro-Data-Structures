
class Dueue(list):

    def __init__(self):
        """Initialize this node with the given data."""
        self = list()

    def enqueue_to_start(self, item):
        self.insert(0, item)

    def enqueue_to_end(self, item):
        self.append(item)

    def dequeue_from_start(self):
        if len(self) is not 0:
            return self.pop(0)
        else:
            return "nothing in queue"

    def dequeue_from_end(self):
        if len(self) is not 0:
            return self.pop(len(self)-1)
        else:
            return "nothing in queue"

    def iterate(self):
        all_items = []
        for item in self:
            all_items.append(item)
        return all_items

def test_queue():
    q = Dueue()
    q.enqueue_to_start((1, 1))
    q.enqueue_to_end((2, 2))
    q.enqueue_to_start((3, 3))
    print(q.iterate())
    print(q.dequeue_from_start())
    print(q.dequeue_from_end())
    print(q.dequeue_from_start())
    print(q.dequeue_from_start())

if __name__ == '__main__':
    test_queue()
