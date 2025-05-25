while True:
    try:
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str)  # Try converting to a float

        num2_str = input("Enter the second number: ")
        num2 = float(num2_str)  # Try converting to a float

        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
        break  # Exit the loop if division is successful
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero second number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")