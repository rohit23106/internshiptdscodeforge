import random
import string
def generate_password(length, include_letters=True, include_digits=True, include_special=True):
    characters = ""
    if include_letters:
        characters += string.ascii_letters  # Adds both lowercase and uppercase letters
    if include_digits:
        characters += string.digits  # Adds digits 0-9
    if include_special:
        characters += string.punctuation  # Adds special characters like !@#$%^&*
    if not characters:
        return "You must select at least one type of character!"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def get_password_requirements():
    length = int(input("Enter the desired password length: "))
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    return length, include_letters, include_digits, include_special
def main():
    print("Welcome to the Password Generator!")
    length, include_letters, include_digits, include_special = get_password_requirements()
    password = generate_password(length, include_letters, include_digits, include_special)
    print(f"Your generated password is: {password}")
main()
