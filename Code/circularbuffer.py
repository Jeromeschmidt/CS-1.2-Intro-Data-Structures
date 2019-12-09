
class CircularBuffer(list):

    def __init__(self, size):
        """Initialize this node with the given data."""
        # self = list()
        self.size = size
        self.ph = 0

    def enqueue(self, item):
        if len(self) < self.size:
            self.append(item)
        else:
            self[self.ph] = item
            self.ph += 1
        if self.ph == self.size:
            self.ph = 0

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
    q = CircularBuffer(5)
    q.enqueue((1, 1))
    q.enqueue((2, 2))
    q.enqueue((3, 3))
    q.enqueue((4, 4))
    q.enqueue((5, 5))
    q.enqueue((6, 6))
    print(q.iterate())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

if __name__ == '__main__':
    test_queue()
