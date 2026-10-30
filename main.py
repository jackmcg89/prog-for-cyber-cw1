from security_tools import (
    generate_strong_password,
    validate_ip,
    validate_password,
)


def main():
    # Ask for both values, then report whether each passes the basic checks.
    password = input("Enter a password: ")
    ip_address = input("Enter an IP address: ")

    if validate_password(password):
        print("Password is valid.")
    else:
        print("Password is not strong enough.")
        print(f"Suggested strong password: {generate_strong_password()}")

    if validate_ip(ip_address):
        print("Valid IP address.")
    else:
        print("Invalid IP address.")


if __name__ == "__main__":
    main()
