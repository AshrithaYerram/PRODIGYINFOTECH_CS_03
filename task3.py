import re

def check_password_strength(password):
    # Define complexity requirements
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Count total issues
    errors = [length_error, uppercase_error, lowercase_error, digit_error, special_char_error]
    score = 5 - sum(errors)  # Higher score means stronger password

    # Password strength levels
    strength_levels = {
        5: "Very Strong 💪",
        4: "Strong ✅",
        3: "Moderate ⚠️",
        2: "Weak ❌",
        1: "Very Weak ❌❌",
        0: "Extremely Weak ❌❌❌"
    }

    return strength_levels[score]

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
