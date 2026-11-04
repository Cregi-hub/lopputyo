def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b


def main():
    while True:
        print("===== CALCULATOR =====")
        print("""
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
        """)

        choice = input("Choose an option: ")

        match choice:
            case "1":
                try:
                    number1 = float(input("Enter first number: "))
                    number2 = float(input("Enter second number: "))

                    result = addition(number1, number2)
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            case "2":
                try:
                    number1 = float(input("Enter first number: "))
                    number2 = float(input("Enter second number: "))

                    result = subtraction(number1, number2)
                    print(f"Result: {result}")

                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            case "3":
                try:
                    number1 = float(input("Enter first number: "))
                    number2 = float(input("Enter second number: "))

                    result = multiplication(number1, number2)
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            case "4":
                print("Division not implemented yet")
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid option!")


if __name__ == "__main__":
    main()
