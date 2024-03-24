import re


def pass_checker(password):
    suggestions = []

    if len(password) < 8:
        return "Weak:Password must be more than 8 characters"  
    if not any(char.isupper() for char in password) and not any (char.islower() for char in password):
        return "Weak: Password must contain an upper and Lower case letter"
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must contain at least one Special character"
    
    return "Strong Password! Well done!"
def main():
    password=input("Enter your password: ")
    Strenght = pass_checker(password)
    print(Strenght)

if __name__ == "__main__":
    main()
