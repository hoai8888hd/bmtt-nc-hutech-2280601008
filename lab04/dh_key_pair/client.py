import os
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Get the absolute path of the current script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'server_public_key.pem')

# Hàm tạo cặp khóa DH cho client
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Hàm tính khóa bí mật chung từ private key của client và public key của server
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

# Chương trình chính
def main():
    try:
        # Ensure the public key file exists
        if not os.path.exists(PUBLIC_KEY_PATH):
            raise FileNotFoundError(f"Public key file not found at {PUBLIC_KEY_PATH}")

        # Load the public key
        with open(PUBLIC_KEY_PATH, "rb") as f:
            server_public_key = serialization.load_pem_public_key(f.read())
            print("Public key loaded successfully!")

        # Tạo tham số DH và khóa cho client
        parameters = server_public_key.parameters()
        private_key, public_key = generate_client_key_pair(parameters)

        # Tính khóa chung
        shared_secret = derive_shared_secret(private_key, server_public_key)

        print("Shared Secret:", shared_secret.hex())

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()