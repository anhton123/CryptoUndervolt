from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

NUM_OF_ITERATIONS = 1000
plaintext = b'\xde\xad\xbe\xef'

start = time.time()
for i in range(NUM_OF_ITERATIONS):
    key = RSA.import_key(open("public.pem").read())
    cipher = PKCS1_OAEP.new(key)
    enc_plaintext = cipher.encrypt(plaintext)
    #print(str(list(enc_plaintext)))
end = time.time()
print(end-start)