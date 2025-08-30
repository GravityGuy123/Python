def create_multiplier(factor):
    """Creates a function that multiplies by a specific factor"""

    def multiplier(number):
        return number * factor  # 'factor' is captured from outer scope

    return multiplier


# Create specialized functions
double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15

# def greet():
#     print("Hello!")
#     print("Nice to meet you!")
#     print("Have a great day!")

# greet()

def sum(a, b):
    return a + b

print(sum(2, 3))


def exp(num1, num2):
    print(num1 * num2)

exp(4, 10)