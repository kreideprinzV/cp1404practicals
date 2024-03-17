def main():
    """The main function that runs the program.
    """
    email_directory = get_emails_and_names()
    print_email_directory(email_directory)
def extract_name_from_email(email):
    """Extracts a potential name from the email address before the domain part.
    """
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').replace('_', ' ').replace('-', ' ').split()
    name = ' '.join(parts).title()
    return name

def get_name(email):
    """Get the name from the user or use the extracted name if the user accepts it.
    """
    extracted_name = extract_name_from_email(email)
    user_input = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()
    if user_input in ['', 'y', 'yes']:
        return extracted_name
    else:
        return input("Name: ").title()

def get_emails_and_names():
    """Gathers emails and names from the user until they enter a blank email.
    """
    email_to_name = {}
    email = input("Email: ")
    while email:
        name = get_name(email)
        email_to_name[email] = name
        email = input("Email: ")
    return email_to_name

def print_email_directory(email_to_name):
    """Prints out the email directory.
    """
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
