# collect user preferences
# length
# should contain uppercase
# should contain special
# should contain digits

# create all available characters
# randomly pick characters up to the length
# ensure we have at least one of each charaacter type
# ensure lenght is valid

import random
import string   

def generate_password():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired password length (minimum 4): "))
    while length < 4:
        print("Password length should be at least 4.")
        length = int(input("Enter the desired password length (minimum 4): "))
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    special_chars = string.punctuation if use_special else ''
    digit_chars = string.digits if use_digits else ''
    
    all_chars = lowercase_chars + uppercase_chars + special_chars + digit_chars
    
    if not all_chars:
        print("No character types selected. Cannot generate password.")
        return
    
    password = []
    
    # Ensure at least one character from each selected type
    password.append(random.choice(lowercase_chars))
    if use_uppercase:
        password.append(random.choice(uppercase_chars))
    if use_special:
        password.append(random.choice(special_chars))
    if use_digits:
        password.append(random.choice(digit_chars))
    
    while len(password) < length:
        password.append(random.choice(all_chars))
    
    random.shuffle(password)
    
    generated_password = ''.join(password)
    print(f"Generated Password: {generated_password}")


generate_password()