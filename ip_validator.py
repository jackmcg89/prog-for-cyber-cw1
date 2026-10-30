def validate_ip(ip_address: str) -> bool:
    """Check that an IP address has four numeric octets from 0 to 255."""
    if not isinstance(ip_address, str):
        return False

    candidate = ip_address.strip()
    if "." not in candidate or candidate.count(".") != 3:
        return False

    parts = candidate.split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        if not part or not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False

    return True


def main():
    ip_address = input("Enter an IP address: ")
    if validate_ip(ip_address):
        print("Valid IP address")
    else:
        print("Invalid IP address")


if __name__ == "__main__":
    main()
