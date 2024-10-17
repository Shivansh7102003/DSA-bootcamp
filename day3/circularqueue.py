class CircularQueue():
    def __init__(self, size):
        self.maxsize = size
        self.queueArray = [0] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def isFull(self):
        return (self.rear + 1) % self.maxsize == self.front

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full. Cannot enqueue.")
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queueArray[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.maxsize
            self.queueArray[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return -1
        item = self.queueArray[self.front]
        if self.front == self.rear:  # Only one element was present
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.maxsize
        return item

    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        index = self.front
        while True:
            print(self.queueArray[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.maxsize
        print()

# Example usage
circularQueue = CircularQueue(5)
circularQueue.enqueue(1)
circularQueue.enqueue(2)
circularQueue.enqueue(3)
circularQueue.display()  # Output: 1 2 3
