import random
import string

def main():
    # 1. Välkomstmeddelande
    print("Welcome to this random password generator")
    
while True:
    try:
        # 2. Längd-input och validering
        length = int(input("Enter password length (8-24): "))
        if 8 <= length <= 24:
            print(f"Length chosen is {length}")
            break
        else:
            print("Enter a number between 8-24") 
    except ValueError:
        print("Please enter a valid number")
            
# 3. Få val för varje teckentyp (y/n för var och en)
upper_case = input("Do you want Uppercase Letters? (y/n): ").lower()
lower_case = input("Do you want Lowercase Letters? (y/n): ").lower()
numbers = input("Do you want Numbers (123456)? (y/n): ").lower()
characters = input("Do you want Special characters (!#¤%&)? (y/n): ").lower()
            
# 4. Bygg character_pool baserat på val
character_pool = ""
        
if upper_case == "y":
    character_pool += string.ascii_uppercase
            
if lower_case == "y":
    character_pool += string.ascii_lowercase
            
if numbers == "y":
    character_pool += string.digits
            
if characters == "y":
    character_pool += string.punctuation
        
# 5. Generera lösenord med random.choice()
password = []
for i in range(length):
    password.append(random.choice(character_pool))
            
# 6. Visa resultat
password_string = "".join(password)
print(f"\033[33mYour new password is: \033[0m\n{password_string}")

