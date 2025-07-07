def sanitize_input(user_input):
    """Sanitize user input to prevent injection"""
    dangerous_chars = ['<', '>', '&', '"', "'"]
    for char in dangerous_chars:
        user_input = user_input.replace(char, '')
    return user_input
