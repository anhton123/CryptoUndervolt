from Crypto.Cipher import AES
import time

NUM_OF_ITERATIONS = 20000
plaintext = b'\xde\xad\xbe\xef'
key = b'\x12\x34\x56\x78\x90\xab\xcd\xef\x12\x34\x56\x78\x90\xab\xcd\xef'

start = time.time()
for i in range(NUM_OF_ITERATIONS):
    cipher = AES.new(key, AES.MODE_GCM)                
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)   
    #print(list(ciphertext))
    #print(list(tag))
    #print(list(cipher.nonce))
end = time.time()
print(end - start)
