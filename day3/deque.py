maxsize = 5
class Deque():
    def __init__(self):
        self.queueArray = []

    def enqueue(self , item):
        if len(self.queueArray)==maxsize:
            print("queue is full", item, "cant be inserted")
        else:
            self.queueArray = self.queueArray + [item]
    def display(self):
        print("the current queue is:" , self.queueArray)
    def dequeue(self):
        if len(self.queueArray) == 0:
            print("queue is empty")
        else:
            self.queueArray = self.queueArray[1:]

    def insertfront(self, data):
        if len(self.queueArray) == maxsize:
            print(f"queue is full{data} cannot be inserted")
        else:
            self.queueArray.insert(0 ,data)

    def deleterear(self):
        if len(self.queueArray)==0:
            print("queue is empty")
        else:
            self.queueArray.pop(-1)


deque = Deque()
deque.enqueue(5)
deque.enqueue(6)
deque.enqueue(7)
deque.display()
deque.insertfront(4)
deque.display()
deque.deleterear()
deque.display()
deque.dequeue()
deque.display()

