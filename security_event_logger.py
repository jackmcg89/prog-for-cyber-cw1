from datetime import datetime


CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "Cyber123!"
CLIENT_IP_ADDRESS = "192.168.1.25"
security_events = []


def record_login_event(username):
    password = input("Enter password: ")
    successful = username == CORRECT_USERNAME and password == CORRECT_PASSWORD

    event = {
        "event_id": len(security_events) + 1,
        "username": username,
        "ip_address": CLIENT_IP_ADDRESS,
        "event": "Successful login" if successful else "Failed login",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    security_events.append(event)

    print("\nSecurity Event Log")
    print("-" * 60)
    print(f"Event ID: {event['event_id']}")
    print(f"Username: {event['username']}")
    print(f"IP Address: {event['ip_address']}")
    print(f"Event: {event['event']}")
    print(f"Timestamp: {event['timestamp']}")
    print("-" * 60)

    return successful


def main():
    print("Login Authentication")
    print("Use the configured account to sign in.")

    while True:
        username = input("\nEnter username: ").strip()
        if record_login_event(username):
            print("Authentication successful.")
            break
        print("Authentication failed. Please try again.")


if __name__ == "__main__":
    main()
