
def load_common_passwords(wordlist_path):
    """Load common passwords from a wordlist file."""
    try:
        with open(wordlist_path, 'r') as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print("Wordlist file not found.")
        return set()

def find_weak_passwords(users, common_passwords):
    weak_users = {}
    for user, password in users.items():
        if password in common_passwords:
            weak_users[user] = password
    return weak_users

    

if __name__ == "__main__":
    # Example user data (username: password)
    users = {
        "user1": "123456",
        "user2": "password",
        "user3": "qwerty",
        "user4": "securepassword123",
        "user5": "letmein"
    }

    # Path to the wordlist file
    wordlist_path = "3/common_passwords.txt"

    # Load common passwords
    common_passwords = load_common_passwords(wordlist_path)

    # Find weak passwords
    weak_users = find_weak_passwords(users, common_passwords)

    # Output results
    if weak_users:
        print("Users with weak passwords:")
        for user, password in weak_users.items():
            print(f"{user}: {password}")
    else:
        print("No weak passwords found.")