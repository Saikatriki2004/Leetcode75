class StockSpanner:
    def __init__(self):
        # Initialize a stack to store tuples of (price, span)
        self.stack = []
        # Initialize a variable to keep track of the current day
        self.current_day = 0
    
    def next(self, price: int) -> int:
        # Increment the current day
        self.current_day += 1
        
        # While there are items in the stack and the price at the top of the stack is less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()  # Remove the price and span from the stack
        
        # Determine the span for the current price
        if not self.stack:
            # If the stack is empty, the span is the entire range of days
            span = self.current_day
        else:
            # Otherwise, calculate the span based on the top of the stack
            span = self.current_day - self.stack[-1][1]
        
        # Push the current price and its span onto the stack
        self.stack.append((price, self.current_day))
        
        return span

# Example usage
stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # Output: 1
print(stockSpanner.next(80))   # Output: 1
print(stockSpanner.next(60))   # Output: 1
print(stockSpanner.next(70))   # Output: 2
print(stockSpanner.next(60))   # Output: 1
print(stockSpanner.next(75))   # Output: 4
print(stockSpanner.next(85))   # Output: 6
