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
