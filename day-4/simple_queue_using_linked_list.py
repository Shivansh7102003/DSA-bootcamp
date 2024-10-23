class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if not new_node:
            print("Memory allocation error")
            return
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{data} enqueued to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return -1
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        dequeued_data = temp.data
        del temp
        return dequeued_data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return -1
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        print("Queue elements are:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

def menu():
    queue = Queue()
    while True:
        print("\n-- Queue Menu --")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            value = int(input("Enter value to enqueue: "))
            queue.enqueue(value)
        elif choice == 2:
            dequeued_value = queue.dequeue()
            if dequeued_value != -1:
                print(f"Dequeued value: {dequeued_value}")
        elif choice == 3:
            peek_value = queue.peek()
            if peek_value != -1:
                print(f"Front value: {peek_value}")
        elif choice == 4:
            queue.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
