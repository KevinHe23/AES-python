from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # Genera una llave aleatoria de 16 bytes.

with open('key.txt', 'wb') as a_file:
    a_file.write(key)

print('Ingrese el texto a encriptar: ', end="")
plaintext = input().encode()

cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

ct = b64encode(ciphertext).decode('utf-8')

print('El texto encriptado es: ', end="")
print(ct)

with open('cipher_text.txt', 'wb') as b_file:
    b_file.write(cipher.iv)
    b_file.write(ciphertext)
