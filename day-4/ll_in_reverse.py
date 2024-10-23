class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None (empty list)

    # Function to insert a new node at the beginning of the list
    def insert(self, value):
        new_node = Node(value)  # Create a new node with the given value
        new_node.next = self.head  # Set the next pointer to the current head
        self.head = new_node  # Update the head to point to the new node

    # Recursive function to print the linked list in reverse order
    def _print_reverse(self, node):
        if node is None:
            return  # Base case: end of the list
        self._print_reverse(node.next)  # Recursively call for the next node
        print(node.data)  # Print the data of the current node after recursion

    # Function to display the linked list in reverse order
    def display_reverse(self):
        if self.head is None:
            print("\nLinked List is Empty!")  # Handle empty list
            return
        print("\nLinked List in reverse order:")
        self._print_reverse(self.head)  # Call the recursive function

# Main function providing a menu-driven interface for the linked list operations
def main():
    linked_list = LinkedList()

    while True:
        print("\n\n*** LINKED LIST MENU ***")
        print("1. Insert")
        print("2. Print in Reverse")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the value to insert: "))
            linked_list.insert(value)
        elif choice == 2:
            linked_list.display_reverse()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("\nInvalid choice! Try again.")

if __name__ == "__main__":
    main()
