import re

def normalize_operators(equation):
    # Replace sequences of the same operator with a single instance of that operator
    equation = re.sub(r'\+\+', '+', equation)  # Replace '++' with '+'
    equation = re.sub(r'\-\-', '-', equation)  # Replace '--' with '-'
    equation = re.sub(r'\*\*', '*', equation)  # Replace '**' with '*'
    equation = re.sub(r'//', '/', equation)    # Replace '//' with '/'
    
    # Replace alternating operators with the first operator
    equation = re.sub(r'([+\-*/]){2,}', r'\1', equation)  # Normalize consecutive different operators

    # Remove operators at the start of the equation if they exist
    equation = re.sub(r'^[+\-*/]+', '', equation)  # Remove leading operators
    # Remove operators at the end of the equation if they exist
    equation = re.sub(r'[+\-*/]+$', '', equation)  # Remove trailing operators

    return equation.strip()  # Remove any leading or trailing whitespace

def calculator():
    try:
        # Take an equation from the user
        equation = input("Enter an equation: ")
        
        # Check if the input contains any invalid characters
        allowed_chars = "0123456789+-*/(). "
        if any(char not in allowed_chars for char in equation):
            raise ValueError("Invalid input! Only numbers, parentheses, and mathematical operators (+, -, *, /) are allowed.")
        
        # Check for mismatched parentheses
        if equation.count('(') != equation.count(')'):
            raise ValueError("Mismatched parentheses! Please check your equation.")

        # Normalize operators
        equation = normalize_operators(equation)

        # Evaluate the equation
        result = eval(equation) if equation else 0  # Default to 0 if the equation is empty
        
        # Output the result
        print(f"The result is: {result}")
    
    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Division by zero is not allowed.")
    
    except (SyntaxError, NameError):
        # Handle syntax errors or undefined variables
        print("Invalid equation! Please enter a valid mathematical expression.")
    
    except ValueError as ve:
        # Handle the custom ValueError for invalid input or mismatched parentheses
        print(ve)
    
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")

# Run the calculator
calculator()
