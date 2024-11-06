class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# Example usage
print("Sum:", Calculator.add(5, 10))
print("Add method called:", Calculator.count, "times")
