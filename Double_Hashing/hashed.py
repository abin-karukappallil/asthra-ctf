import hashlib
import random
import string

def generate_random_password(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_hashed_password(password):
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    md5_hash = hashlib.md5(sha256_hash.encode()).hexdigest()
    return md5_hash

password = generate_random_password()
hashed_password = create_hashed_password(password)
with open('hashed_password.txt', 'w') as file:
    file.write(hashed_password)

print(f"Generated password: {password}")
print(f"Hashed password (SHA256 -> MD5): {hashed_password}")
