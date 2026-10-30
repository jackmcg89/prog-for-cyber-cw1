def main():
    # Store the initial details for a security incident.
    incident = {
        "username": "admin",
        "ip_address": "192.168.1.25",
        "event_type": "Failed login",
        "risk_level": "Medium",
    }

    # Display the username and IP address before updating the incident.
    print(f"Username: {incident['username']}")
    print(f"IP Address: {incident['ip_address']}")

    # Add a status and update the incident risk level.
    incident["status"] = "Under investigation"
    incident["risk_level"] = "High"

    # Remove the event type field from the incident record.
    incident.pop("event_type")

    # Show the remaining incident information and the number of fields.
    print("\nRemaining incident details:")
    for key, value in incident.items():
        print(f"{key}: {value}")

    print(f"\nTotal key-value pairs: {len(incident)}")


if __name__ == "__main__":
    main()
