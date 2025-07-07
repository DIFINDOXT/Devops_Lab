#!/usr/bin/env python3

def main():
    print("DevOps Practice App - Version 1.0.0")

def authenticate_user(username, password):
    if username == "admin" and password == "secret":
        print("Login successful.")
        return True
    else:
        print("Invalid credentials.")
        return False

if __name__ == "__main__":
    main()

Bug introduced here
Temporary debug line
import requests
print('Starting API integration...')

def fetch_external_data(url):
    """Fetch data from external API"""
    try:
        response = requests.get(url, timeout=10)
        return response.json()
    except Exception as e:
        print(f"API call failed: {e}")
        return None
