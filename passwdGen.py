import random

password_size = int(input("size: "))
char_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char = char_ + char_.lower() + '!@#$%^&*()_"+-=\'[]{};:,\.|<>/? ' + '0123456789'


def password(size):
    passwd = ''
    for _ in range(size):
        passwd += char[random.randint(0, len(char) - 1)]
    print(passwd)

password(password_size)


