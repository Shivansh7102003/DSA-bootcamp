class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

class Lift:
    def __init__(self, num_floors):
        self.current_floor = 1
        self.num_floors = num_floors
        self.direction = "up"
        self.requests = Queue()

    def request_floor(self, floor):
        if 1 <= floor <= self.num_floors:
            self.requests.enqueue(floor)
            print(f"Floor {floor} requested.")
        else:
            print(f"Invalid floor request: {floor}")

    def move(self):
        if not self.requests.is_empty():
            destination = self.requests.dequeue()
            print(f"Moving from floor {self.current_floor} to floor {destination}")
            self.current_floor = destination
        else:
            print("No pending requests.")

    def run(self):
        while not self.requests.is_empty():
            self.move()
        print("All requests completed.")

# Example usage
lift = Lift(10)  # number of floors to be in lift

# floor on which to go/requests
lift.request_floor(5)
lift.request_floor(2)
lift.request_floor(8)
lift.request_floor(1)
lift.request_floor(2)
lift.request_floor(4)
lift.request_floor(5)
lift.request_floor(8)


# Run the lift
lift.run()