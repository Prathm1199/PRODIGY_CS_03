import re

def check_password(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search("[a-z]", password):
        return "Weak: No lowercase letter"
    if not re.search("[A-Z]", password):
        return "Weak: No uppercase letter"
    if not re.search("[0-9]", password):
        return "Weak: No number"
    if not re.search("[@#$%^&+=]", password):
        return "Weak: No special character"
    return "Strong Password"

# Test examples
password1 = "Pass123"
password2 = "Pass@123"
password3 = "weak"

print(f"Password: {password1} => {check_password(password1)}")
print(f"Password: {password2} => {check_password(password2)}")
print(f"Password: {password3} => {check_password(password3)}")
