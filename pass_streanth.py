import re

def evaluate_password_strength(password):
    # Define the criteria for a strong password
    min_length = 8
    special_characters = r'[\W_]'  # Non-word characters or underscores

    # Check password length
    if len(password) < min_length:
        return "Password is too short. It must be at least 8 characters long."

    # Check for the presence of uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    # Check for the presence of lowercase letters
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    # Check for the presence of digits
    if not re.search(r'\d', password):
        return "Password must contain at least one digit."

    # Check for the presence of special characters
    if not re.search(special_characters, password):
        return "Password must contain at least one special character."

    return "Password is strong."

# Example usage
password = input("Enter your password: ")
print(evaluate_password_strength(password))
