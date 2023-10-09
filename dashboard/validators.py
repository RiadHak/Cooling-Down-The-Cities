from argon2 import PasswordHasher

def HashPW(password):
    passwordh = PasswordHasher()
    hashing = passwordh.hash(password).encode('utf-8')
    return (hashing, passwordh)