class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front  # Make it circular
        print(f"Enqueued {value} into the circular queue.")

    def dequeue(self):
        if self.is_empty():
            print("Circular queue is empty! Cannot dequeue.")
            return -1
        dequeued_value = self.front.data
        if self.front == self.rear:
            # Only one element in the queue
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  # Maintain circular structure
        print(f"Dequeued {dequeued_value} from the circular queue.")
        return dequeued_value

    def display(self):
        if self.is_empty():
            print("Circular queue is empty.")
            return
        temp = self.front
        print("Circular Queue elements:", end=" ")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:  # Loop until we reach the front again
                break
        print()

def menu():
    queue = CircularQueue()
    while True:
        print("\nCircular Queue Operations Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the element to enqueue: "))
            queue.enqueue(value)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
