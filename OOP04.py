class Calculator:
    """A simple calculator class with utility functions."""

    @staticmethod
    def add(x, y):
        """Adds two numbers."""
        return x + y

    @staticmethod
    def subtract(x, y):
        """Subtracts two numbers."""
        return x - y

    @staticmethod
    def multiply(x, y):
        """Multiplies two numbers."""
        return x * y

    @staticmethod
    def is_even(num):
        """Checks if a number is even."""
        return num % 2 == 0

# --- Using the static methods ---

# You don't need to create an instance like `calc = Calculator()`
# You just call the methods directly on the class.

sum_result = Calculator.add(15, 7)
print(f"15 + 7 = {sum_result}")
# Output: 15 + 7 = 22

difference = Calculator.subtract(10, 4)
print(f"10 - 4 = {difference}")
# Output: 10 - 4 = 6

print(f"Is 5 even? {Calculator.is_even(5)}")
# Output: Is 5 even? False