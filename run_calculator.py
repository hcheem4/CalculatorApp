from calculator import add, subtract, multiply, divide

def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print(f"The result is: {add(num1, num2)}")
    elif choice == "2":
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == "4":
        try:
            print(f"The result is: {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
