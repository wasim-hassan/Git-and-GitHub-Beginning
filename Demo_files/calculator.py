import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Signature
print("--THE--CALCULATOR--")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            logging.warning("Invalid input. User must enter a numeric value.")
            print("Invalid input. Please enter a numeric value.")

def calculator():
    logging.info("Calculator started.")
    print("Simple Calculator")
    print("Enter the first number, the operator, then the second number.")

    continue_calculation = True

    while continue_calculation:
        try:
            num1 = get_numeric_input("Enter the first number: ")
            operation = input("Enter operator (+, -, *, /): ").strip()

            if operation not in ('+', '-', '*', '/'):
                logging.warning(f"Invalid operator: {operation}")
                print("Invalid operator. Please select one of (+, -, *, /).")
                continue

            num2 = get_numeric_input("Enter the second number: ")

            if operation == '+':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
                logging.info(f"Performed addition: {num1} + {num2} = {result}")
            elif operation == '-':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
                logging.info(f"Performed subtraction: {num1} - {num2} = {result}")
            elif operation == '*':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
                logging.info(f"Performed multiplication: {num1} * {num2} = {result}")
            elif operation == '/':
                try:
                    result = divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
                    logging.info(f"Performed division: {num1} / {num2} = {result}")
                except ValueError as e:
                    logging.error(e)
                    print(e)

            next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if next_calculation != 'yes':
                logging.info("Calculator session ended by user.")
                print("Thank you for using Wasim's calculator. Goodbye!")
                continue_calculation = False

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    calculator()
