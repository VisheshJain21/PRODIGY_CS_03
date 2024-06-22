import re

def check_password_complexity(password):
    # Minimum length check
    if len(password) < 8:
        return "Weak - Password should be at least 8 characters long."
    
    # Check for presence of uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak - Password should contain at least one uppercase letter."
    
    # Check for presence of lowercase letters
    if not any(char.islower() for char in password):
        return "Weak - Password should contain at least one lowercase letter."
    
    # Check for presence of numbers
    if not any(char.isdigit() for char in password):
        return "Weak - Password should contain at least one number."
    
    # Check for presence of special characters
    if not re.search("[!@#$%^&*()_+=\-{}\[\]:;\"'|\\<,>.?/]", password):
        return "Weak - Password should contain at least one special character."
    
    # If all checks pass, the password is strong
    return "Strong - Password meets complexity criteria."

# Example usage
password = input("Enter your password: ")
result = check_password_complexity(password)
print(result)
