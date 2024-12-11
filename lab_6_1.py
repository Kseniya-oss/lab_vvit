import hashlib
import os

class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email

        self.salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.salt, 100000)
        self.password = key


    def set_password(self, new_password):
        key = hashlib.pbkdf2_hmac('sha256', new_password.encode('utf-8'), self.salt, 100000)
        self.password = key

    def check_password(self, password_):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password_.encode('utf-8'), self.salt,100000)
        if key == self.password: return True
        else: return False

my_account = UserAccount('Kseniya', 'email', 'password123')

# password = input('Введите свой пароль: ')
# result = my_account.check_password(password)

# new_password = input('Введите новый пароль: ')
# my_account.set_password(new_password)

