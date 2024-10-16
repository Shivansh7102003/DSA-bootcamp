maxsize = 3
class Queue():
    def __init__(self):
        self.queue = []
    def is_empty(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            return None
    def is_full(self):
        if len(self.queue)==maxsize:
            print("queue is full")
        else:
            return None
    def enque(self , item):
        if len(self.queue)==maxsize:
            print("queue is full", item, "cant be inserted")
        else:
            self.queue = self.queue + [item]
    def display(self):
        if self.is_empty():
            print("queue is empty")
        else:
            print("the current queue is:" , self.queue)
    def deque(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            self.queue = self.queue[1:]

queue = Queue()

queue.enque(5)
queue.enque(6)
queue.enque(7)

queue.display()

queue.enque(8)

queue.deque()
queue.display()




