import ecdsa
import os

# Get the absolute path of the current script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEYS_DIR = os.path.join(BASE_DIR, 'keys')

# Tạo thư mục chứa khóa nếu chưa tồn tại
if not os.path.exists(KEYS_DIR):
    os.makedirs(KEYS_DIR)

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()  # Tạo khóa riêng tư
        vk = sk.get_verifying_key()  # Lấy khóa công khai từ khóa riêng tư
        
        # Lưu khóa riêng tư
        with open(os.path.join(KEYS_DIR, 'privateKey.pem'), 'wb') as p:
            p.write(sk.to_pem())

        # Lưu khóa công khai
        with open(os.path.join(KEYS_DIR, 'publicKey.pem'), 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        # Đọc khóa riêng tư từ file
        with open(os.path.join(KEYS_DIR, 'privateKey.pem'), 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        # Đọc khóa công khai từ file
        with open(os.path.join(KEYS_DIR, 'publicKey.pem'), 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, key):
        # Ký dữ liệu bằng khóa riêng tư
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        _, vk = self.load_keys()
        try:
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False
