# Simple calculator with functions

#Define functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Handle division by zero
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main function to perform calculations
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice =='3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice =='4':
            print(f"The result is: {divide(num1, num2)}")
         
    else:
        print("Invalid Input")
        
        
calculator()
    