from collections import deque

class Order:
    def __init__(self, order_id, description, priority=False):
        self.order_id = order_id
        self.description = description
        self.priority = priority
    
    def __repr__(self):
        return f"Order({self.order_id}, {self.description}, {'Priority' if self.priority else 'Regular'})"

class KitchenQueue:
    def __init__(self):
        """Initialize an empty queue for orders."""
        self.orders = deque()
        self.priority_stack = []

    def add_order(self, order_id, description, priority=False):
        """Add a new order to the queue or priority stack."""
        order = Order(order_id, description, priority)
        if priority:
            self.priority_stack.append(order)
            print(f"Added {order} to the priority stack.")
        else:
            self.orders.append(order)
            print(f"Added {order} to the queue.")

    def complete_order(self):
        """Complete an order, preferring priority orders first."""
        if self.priority_stack:
            completed_order = self.priority_stack.pop()
            print(f"Completed {completed_order} from the priority stack.")
            return completed_order
        elif self.orders:
            completed_order = self.orders.popleft()
            print(f"Completed {completed_order} from the queue.")
            return completed_order
        else:
            print("No orders to complete.")
            return None

    def display_orders(self):
        """Display all orders in the queue and priority stack."""
        print("Current Orders in Queue:")
        for order in self.orders:
            print(order)
        print("Current Priority Orders in Stack:")
        for order in reversed(self.priority_stack):
            print(order)

# Testing the KitchenQueue class
if __name__ == "__main__":
    kitchen_queue = KitchenQueue()
    
    # Add some orders
    kitchen_queue.add_order(1, "Burger")
    kitchen_queue.add_order(2, "Pizza", priority=True)
    kitchen_queue.add_order(3, "Pasta")
    kitchen_queue.add_order(4, "Salad", priority=True)
    
    # Display current orders
    kitchen_queue.display_orders()
    
    # Complete some orders
    kitchen_queue.complete_order()
    kitchen_queue.complete_order()
    
    # Display remaining orders
    kitchen_queue.display_orders()
    
    # Complete remaining orders
    kitchen_queue.complete_order()
    kitchen_queue.complete_order()
    
    # Try to complete an order from an empty queue and stack
    kitchen_queue.complete_order()
