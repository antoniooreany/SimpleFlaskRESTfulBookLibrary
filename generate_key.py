# generate_key.py
import secrets

secret_key = secrets.token_hex(16)
print(f"Generated secret key: {secret_key}")
