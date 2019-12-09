
class Queue(list):

    def __init__(self):
        """Initialize this node with the given data."""
        self = list()

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        if len(self) is not 0:
            return self.pop(0)
        else:
            return "nothing in queue"

    def iterate(self):
        all_items = []
        for item in self:
            all_items.append(item)
        return all_items

def test_queue():
    q = Queue()
    q.enqueue((1, 1))
    q.enqueue((2, 2))
    q.enqueue((3, 3))
    print(q.iterate())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

if __name__ == '__main__':
    test_queue()
