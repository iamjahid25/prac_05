"""
Emails
Estimate: 45 minutes
Actual:   60 minutes
"""

def get_name_from_email(email):
    """Extract a name from an email address."""
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name


def main():
    """Save names and email addresses together, then show them."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm != "" and confirm != "y":
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

main()
