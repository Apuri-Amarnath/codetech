def add(x, y):
    """Function to perform addition."""
    return x + y

def subtract(x, y):
    """Function to perform subtraction."""
    return x - y

def multiply(x, y):
    """Function to perform multiplication."""
    return x * y

def divide(x, y):
    """Function to perform division."""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def exponentiate(x, y):
    """Function to perform exponentiation."""
    try:
        result = x ** y
        return result
    except OverflowError:
        return "Error too large numbers! "


def main():
    """Main function to execute the calculator."""
    print("Welcome to Simple Calculator with Advanced Features!")
    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Quit")

        choice = input("Enter the operation number or 'q' to quit: ")

        if choice.lower() in ('q', 'quit'):
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", exponentiate(num1, num2))
        else:
            print("Invalid choice. Please enter a valid operation number.")

if __name__ == "__main__":
    main()
