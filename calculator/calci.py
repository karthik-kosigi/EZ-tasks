class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero!"
        return num1 / num2


def print_menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    calculator = Calculator()

    while True:
        print("\n===== Basic Calculator Menu =====")
        print_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = calculator.add(num1, num2)
            print("Result:", result)

        elif choice == '2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = calculator.subtract(num1, num2)
            print("Result:", result)

        elif choice == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = calculator.multiply(num1, num2)
            print("Result:", result)

        elif choice == '4':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                result = calculator.divide(num1, num2)
                print("Result:", result)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4/5).")


if __name__ == "__main__":
    main()
