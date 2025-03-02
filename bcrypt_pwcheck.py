import bcrypt
import sys

# some random, you can add more, weak passwords list
weak_passwords = [
    "123456", "password", "admin", "admin123", "qwerty", "letmein",
    "welcome", "passw0rd", "password123", "12345678", "monkey",
    "abc123", "1q2w3e4r", "adminadmin", "123123"
]

def load_file(filename):
    """Reads a file and returns a list of non-empty lines."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"[ERROR] File '{filename}' not found.")
        sys.exit(1)

def check_weak_passwords(hashes, password_list):
    """
    Tries a list of passwords against multiple bcrypt hashes.
    Prints the result clearly after scanning.
    """
    found_any = False  # Flag to track if any passwords were found

    for hash_index, hashed_password in enumerate(hashes):
        for password in password_list:
            if bcrypt.checkpw(password.encode(), hashed_password.encode()):
                print(f"[✔️ FOUND] Hash {hash_index+1} matches: '{password}'")
                found_any = True
                break  # Stop checking this hash after finding a match

    # Results
    if found_any:
        print("\n[✔️ SUMMARY] At least one match was found!")
    else:
        print("\n[❌ NOTHING FOUND] No password matches any hash.")

def main():
    # Ensure proper usage
    if len(sys.argv) < 2:
        print("Usage: python bcrypt_decrypt.py <hash_file.txt> [password_list.txt]")
        sys.exit(1)

    # Load hashes from file
    hash_file = sys.argv[1]
    hashes = load_file(hash_file)

    # Load password list if provided, else use default weak passwords
    password_list = load_file(sys.argv[2]) if len(sys.argv) > 2 else weak_passwords

    # Run the password check
    check_weak_passwords(hashes, password_list)

if __name__ == "__main__":
    main()
