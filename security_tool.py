CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "Cyber123!"
BRUTE_FORCE_PASSWORD = "password123"
MAX_LOGIN_ATTEMPTS = 3
MAX_BRUTE_FORCE_ATTEMPTS = 5
PASSWORD_COUNTER_ATTEMPTS = 10


def security_event_counter():
    correct_count = 0
    incorrect_count = 0

    for attempt in range(1, PASSWORD_COUNTER_ATTEMPTS + 1):
        password = input(
            f"Enter password ({attempt}/{PASSWORD_COUNTER_ATTEMPTS}): "
        )
        if password == CORRECT_PASSWORD:
            correct_count += 1
        else:
            incorrect_count += 1

    incorrect_percentage = incorrect_count / PASSWORD_COUNTER_ATTEMPTS * 100
    print(f"Correct passwords: {correct_count}")
    print(f"Incorrect passwords: {incorrect_count}")
    print(f"Incorrect password percentage: {incorrect_percentage:.1f}%")

    if incorrect_percentage > 50:
        print("ALERT: More than 50% of passwords entered were incorrect.")


def brute_force_simulation():
    for attempt in range(1, MAX_BRUTE_FORCE_ATTEMPTS + 1):
        guess = input(
            f"Enter password guess ({attempt}/{MAX_BRUTE_FORCE_ATTEMPTS}): "
        )
        if guess == BRUTE_FORCE_PASSWORD:
            print(f"Correct password entered in {attempt} attempt(s).")
            return

        print("Incorrect password.")

    print("Maximum number of attempts reached.")


def login_authentication():
    for attempt in range(1, MAX_LOGIN_ATTEMPTS + 1):
        username = input("Enter username: ").strip()
        password = input("Enter password: ")

        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            print("Authentication succeeded.")
            return True

        print("Authentication failed.")
        if attempt < MAX_LOGIN_ATTEMPTS:
            print(f"Please try again. {MAX_LOGIN_ATTEMPTS - attempt} attempt(s) remaining.")

    print("Account frozen for 24 hours.")
    return False


def main():
    print("Security Tool Login")
    if not login_authentication():
        return

    while True:
        print("\nSecurity Tool Menu")
        print("1. Security Event Counter")
        print("2. Brute-Force Simulation")
        print("3. Login Authentication")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            security_event_counter()
        elif choice == "2":
            brute_force_simulation()
        elif choice == "3":
            if not login_authentication():
                return
        elif choice == "4":
            print("Thank you for using the security tool")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
