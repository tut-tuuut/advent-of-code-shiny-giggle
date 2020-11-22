import string

santa_current_password = 'cqjxjnds'

letters = list(string.ascii_lowercase)
digits = (list(string.digits) + letters)[:26]
print(digits)
print(len(digits))

def password_to_integer(password):
    for digit, letter in zip(digits, letters):
        password = password.replace(letter,digit)
    return int(password, 26)

def integer_to_password(integer):
    if integer < 26:
        return letters[integer%26]
    else:
        return f'{integer_to_password(integer//26)}{letters[integer%26]}'


def increment_password(password, increment=1):
    intpassword = password_to_integer(password)
    intpassword = intpassword + increment
    return integer_to_password(intpassword)


print(password_to_integer('zaza'))
print(integer_to_password(440050))

print(increment_password('zaza',100))