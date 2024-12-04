import json

FILE_NAME = "contacts.json"

def save_to_file(contacts):
    """Save contacts to a JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file)

def load_from_file():
    """Load contacts from a JSON file."""
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
