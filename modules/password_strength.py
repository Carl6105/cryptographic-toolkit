import re

def evaluate_password_strength(password: str) -> dict:
    score = 0
    messages = []

    length = len(password)
    if length >= 12:
        score += 1
    else:
        messages.append("Password should be at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        messages.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("Include at least one number.")

    if re.search(r"[!@#$%^&*()\-_=+{}\[\]:;\"'<>,.?/\\|`~]", password):
        score += 1
    else:
        messages.append("Include at least one special character.")

    common = ["password", "123456", "qwerty", "admin", "letmein"]
    if any(word in password.lower() for word in common):
        messages.append("Avoid common words or patterns in your password.")
        score = max(score - 1, 0)

    return {
        "score": score,
        "messages": messages if messages else ["Strong password!"]
    }
