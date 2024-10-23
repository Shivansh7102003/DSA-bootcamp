class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class Deque:
    def __init__(self):
        self.front = None  # Pointer to the front node
        self.rear = None   # Pointer to the rear node

    # Function to check if the deque is empty
    def is_empty(self):
        return self.front is None

    # Function to add an element at the front of the deque
    def add_front(self, value):
        new_node = Node(value)
        new_node.next = self.front  # Link the new node to the current front
        new_node.prev = None  # New node will be the first node

        if self.is_empty():
            self.rear = new_node  # If deque is empty, set rear to the new node
        else:
            self.front.prev = new_node  # Link the current front's prev to the new node

        self.front = new_node  # Update front to the new node
        print(f"Added {value} to the front of the deque.")

    # Function to add an element at the rear of the deque
    def add_rear(self, value):
        new_node = Node(value)
        new_node.next = None  # New node will be the last node
        new_node.prev = self.rear  # Link the new node to the current rear

        if self.is_empty():
            self.front = new_node  # If deque is empty, set front to the new node
        else:
            self.rear.next = new_node  # Link the current rear to the new node

        self.rear = new_node  # Update rear to the new node
        print(f"Added {value} to the rear of the deque.")

    # Function to remove an element from the front of the deque
    def remove_front(self):
        if self.is_empty():
            print("Deque is empty! Cannot remove from front.")
            return -1

        removed_value = self.front.data  # Store the value to return
        self.front = self.front.next  # Update front to the next node

        if self.front is not None:
            self.front.prev = None  # Update the previous pointer of the new front
        else:
            self.rear = None  # If deque is now empty, update rear to None

        print(f"Removed {removed_value} from the front of the deque.")
        return removed_value

    # Function to remove an element from the rear of the deque
    def remove_rear(self):
        if self.is_empty():
            print("Deque is empty! Cannot remove from rear.")
            return -1

        removed_value = self.rear.data  # Store the value to return
        self.rear = self.rear.prev  # Update rear to the previous node

        if self.rear is not None:
            self.rear.next = None  # Update the next pointer of the new rear
        else:
            self.front = None  # If deque is now empty, update front to None

        print(f"Removed {removed_value} from the rear of the deque.")
        return removed_value

    # Function to display the elements in the deque
    def display(self):
        if self.is_empty():
            print("Deque is empty.")
            return

        temp = self.front
        print("Deque elements:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Main function to demonstrate deque operations
def main():
    deque = Deque()

    while True:
        print("\nDeque Operations Menu:")
        print("1. Add to Front")
        print("2. Add to Rear")
        print("3. Remove from Front")
        print("4. Remove from Rear")
        print("5. Display")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the element to add to the front: "))
            deque.add_front(value)
        elif choice == 2:
            value = int(input("Enter the element to add to the rear: "))
            deque.add_rear(value)
        elif choice == 3:
            deque.remove_front()
        elif choice == 4:
            deque.remove_rear()
        elif choice == 5:
            deque.display()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    # Free the deque memory (Python handles garbage collection automatically)
    while not deque.is_empty():
        deque.remove_front()

if __name__ == "__main__":
    main()
