def validate_name(name):
    """Validate that the name is a string."""
    if not name.isalpha():
        raise ValueError("Error: Name must be a string.")

def validate_email(email):
    """Validate email format."""
    if "@" not in email or "." not in email.split("@")[1]:
        raise ValueError("Error: Invalid email format.")

def validate_phone(phone):
    """Validate that the phone is numeric."""
    if not phone.isdigit():
        raise ValueError("Error: Phone number must be numeric.")
