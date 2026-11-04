def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


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
                    luku1 = float(input("Enter first number: "))
                    luku2 = float(input("Enter second number: "))

                    result = addition(luku1, luku2)
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            case "2":
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))

                    result = subtraction(a, b)
                    print(f"Result: {result}")

                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            case "3":
                print("Multiplication not implemented yet")
            case "4":
                print("Division not implemented yet")
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid option!")


if __name__ == "__main__":
    main()
