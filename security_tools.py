import secrets
import string


MIN_PASSWORD_LENGTH = 8


def validate_password(password: str) -> bool:
    """Check that a password has sufficient length and character variety."""
    if not isinstance(password, str) or len(password) < MIN_PASSWORD_LENGTH:
        return False

    has_letter = any(character.isalpha() for character in password)
    has_digit = any(character.isdigit() for character in password)
    has_symbol = any(not character.isalnum() for character in password)
    return has_letter and has_digit and has_symbol


def validate_ip(ip_address: str) -> bool:
    """Check for four dot-separated numeric octets in the range 0 to 255."""
    if not isinstance(ip_address, str):
        return False

    parts = ip_address.strip().split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        if not part or not part.isdigit() or not 0 <= int(part) <= 255:
            return False

    return True


def generate_strong_password() -> str:
    """Generate a random 10-16 character password with mixed character types."""
    length = secrets.choice(range(10, 17))
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure each required character type appears, then securely shuffle.
    password_characters = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]
    password_characters.extend(
        secrets.choice(all_characters) for _ in range(length - 4)
    )
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)
