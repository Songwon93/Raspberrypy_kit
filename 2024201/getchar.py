try:
    while True:
        userInput = input("Enter a letter or number: ")

        if len(userInput) == 1:
            if userInput.isalpha():
                if userInput == 'z':
                    print('a')
                else:
                    next_letter = chr(ord(userInput) + 1)
                    print(next_letter)
            elif userInput.isdigit():
                print(int(userInput) + 1)
            else:
                print("Invalid input. Please enter a single letter or a number.")
        else:
            print("Invalid input. Please enter a single character.")

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
