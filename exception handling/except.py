try:
    # Ask the user for a number
    number = input("Enter a number: ")
    # Try to convert the input to an integer
    result = int(number)
    print(f"You entered a valid number: {result}")

except ValueError:
    # Handle the case where the input cannot be converted to an integer
    print("Error: Please enter a valid integer!")


