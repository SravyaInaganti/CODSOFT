import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            # Prompt the user to enter the desired length of the password
            length = int(input("Enter the desired length of the password: "))
            
            if length <= 0:
                print("Please enter a positive number.")
                continue

            # Generate and display the password
            password = generate_password(length)
            print(f"Generated password: {password}")
            break
            
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()
