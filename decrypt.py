from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open('key.txt', 'rb') as a_file:
    key = a_file.read()

with open('cipher_text.txt', 'rb') as b_file:
    iv = b_file.read(16)
    ciphertext = b_file.read()

plaintext = AES.new(key, AES.MODE_CBC, iv)

pt = unpad(plaintext.decrypt(ciphertext), AES.block_size)
p_t = str(pt, 'utf-8')

print('El texto desencriptado es: ', end="")
print(p_t)

with open('plain_text.txt', 'wb') as c_file:
    c_file.write(pt)
