import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Criteria 2: Lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Criteria 3: Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Criteria 4: Digit
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one digit.")

    # Criteria 5: Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character (e.g., !, @, #, etc.).")

    # Strength rating
    if strength == 5:
        result = "Very Strong"
    elif strength >= 4:
        result = "Strong"
    elif strength >= 3:
        result = "Moderate"
    else:
        result = "Weak"

    return result, feedback

# Example usage
password = input("Enter a password to test: ")
strength_result, tips = check_password_strength(password)

print("\nPassword Strength:", strength_result)
if tips:
    print("Suggestions to improve:")
    for tip in tips:
        print("-", tip)
