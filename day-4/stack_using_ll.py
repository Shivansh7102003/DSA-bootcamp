class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {value} onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return -1
        popped_value = self.top.data
        self.top = self.top.next
        print(f"Popped {popped_value} from the stack.")
        return popped_value

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        temp = self.top
        print("Stack elements: ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

def main():
    stack = Stack()

    while True:
        print("\nStack Operations Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the element to push: "))
            stack.push(value)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    while not stack.is_empty():
        stack.pop()

if __name__ == "__main__":
    main()
