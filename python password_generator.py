import random
import string

def generate_password(length=12):
    """
    Generate a random password.

    Args:
        length (int): Length of the password. Default is 12.

    Returns:
        str: Randomly generated password.
    """
    if length < 4:  # Ensure the password has enough characters for diversity
        raise ValueError("Password length should be at least 4 characters.")

    # Define the character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password includes at least one character from each pool
    all_chars = lowercase + uppercase + digits + symbols
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length with random characters from all pools
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(length))
