def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator  # Equivalent to: my_function = decorator(my_function)
def my_function():
    print("Inside the function")

my_function()