
import string
import secrets


def generate_password(length, include_numbers, include_symbols):

    # Basic character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Password must contain at least one lowercase and uppercase letter
    required_characters = [
        secrets.choice(lowercase),
        secrets.choice(uppercase)
    ]

    # Start with letters
    all_characters = lowercase + uppercase

    # Include numbers if selected
    if include_numbers:
        all_characters += numbers
        required_characters.append(secrets.choice(numbers))

    # Include symbols if selected
    if include_symbols:
        all_characters += symbols
        required_characters.append(secrets.choice(symbols))

    # Check whether the requested length is sufficient
    if length < len(required_characters):
        raise ValueError(
            f"Password length must be at least {len(required_characters)}."
        )

    # Generate remaining characters
    remaining_length = length - len(required_characters)

    for _ in range(remaining_length):
        required_characters.append(secrets.choice(all_characters))

    # Shuffle characters securely
    secrets.SystemRandom().shuffle(required_characters)

    return ''.join(required_characters)


# Main program
print("================================")
print("     SECURE PASSWORD GENERATOR")
print("================================")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        raise ValueError("Password length must be positive.")

    include_numbers = input(
        "Include numbers? (y/n): "
    ).lower() == "y"

    include_symbols = input(
        "Include symbols? (y/n): "
    ).lower() == "y"

    password = generate_password(
        length,
        include_numbers,
        include_symbols
    )

    print("\nYour generated password is:")
    print(password)

except ValueError as error:
    print("Error:", error)
