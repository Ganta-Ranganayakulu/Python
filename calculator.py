def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b
def modulo(a,b):
    if b==0:
        return "Error! Modulo Division by Zero is not allowed."
    return a%b
def calculator():
    while True:
        print("\n===== CALCULATOR =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5.Modulo Division")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '6':
            print("Exiting calculator... Bye!")
            break
        if choice in ('1', '2', '3', '4','5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print("Result:", add(num1, num2))
                elif choice == '2':
                    print("Result:", subtract(num1, num2))
                elif choice == '3':
                    print("Result:", multiply(num1, num2))
                elif choice == '4':
                    print("Result:", divide(num1, num2))
                elif choice == '5':
                    print("Result:", modulo(num1, num2))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select between 1 and 5.")

calculator()
