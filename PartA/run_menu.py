from PartA import interp

def REPL():
    print("insert 'END' to stop.")
    while True:
        text = input('input > ')
        if text == 'END':
            break
        result, error = interp.run('<stdin>', text)

        if error: print(error.as_string())
        elif result: print(result)

def run_full_program(filepath):
    # Check if the file has the correct .lambda extension
    if not filepath.endswith('.lambda'):
        print(f"Error: File '{filepath}' must have a .lambda extension.")
        return

    try:
        with open(filepath, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return
    except IOError:
        print(f"Error: Unable to read file '{filepath}'.")
        return

    content =  content.split('\n')
    print(content)
    for line in content:
        if len(line):
            result, error = interp.run(filepath, line)
            if error:
                print(error.as_string())
            elif result:
                print(result)

def print_menu():
    print("Menu:\n0 - Exit\n1 - Line by line\n2 - Full program")

def handle_choice(choice):
    if choice == '0':
        print("Exiting the program. Goodbye!")
    elif choice == '1':
        REPL()
    elif choice == '2':
        run_full_program("Test.lambda")
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    choice = None
    while choice != '0':
        print_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice)

if __name__ == "__main__":
    main()