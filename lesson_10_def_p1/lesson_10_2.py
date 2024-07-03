# Task 2
def password_gen(length: int, special: bool = False) -> str:
    """
    Returns a password of the given length.
    :param length: The length of the password
    :param special: Whether to include special characters
    :return: The generated password
    """
    import random
    import string

    if not isinstance(length, int):
        raise TypeError('length must be an int')
    if length < 2:
        raise ValueError('length must be at least 2')

    chars = string.ascii_letters + string.digits + string.punctuation if special else ''
    return ''.join(random.sample(chars, length))


print(password_gen(10))
