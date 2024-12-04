contacts = []

def add_contact(name, email, phone, address):
    """Add a new contact after ensuring no duplicate phone numbers."""
    for contact in contacts:
        if contact['phone'] == phone:
            return "Error: This phone number already exists."
    contacts.append({'name': name, 'email': email, 'phone': phone, 'address': address})
    return "Contact added successfully."

def view_contacts():
    """Display all contacts in a user-friendly format."""
    if not contacts:
        return "No contacts found."
    result = "Contact List:\n"
    for idx, contact in enumerate(contacts, 1):
        result += f"{idx}. {contact['name']} - {contact['email']} - {contact['phone']} - {contact['address']}\n"
    return result

def remove_contact(phone):
    """Delete a contact based on the phone number."""
    global contacts
    for contact in contacts:
        if contact['phone'] == phone:
            contacts = [c for c in contacts if c['phone'] != phone]
            return "Contact removed successfully."
    return "Error: Contact not found."

def search_contact(query):
    """Search for a contact by name, email, phone, or address."""
    results = [c for c in contacts if query.lower() in str(c.values()).lower()]
    if not results:
        return "No matching contacts found."
    result = "Search Results:\n"
    for contact in results:
        result += f"{contact['name']} - {contact['email']} - {contact['phone']} - {contact['address']}\n"
    return result
