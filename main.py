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
                print("Addition not implemented yet")
            case "2":
                print("Subtraction not implemented yet")
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