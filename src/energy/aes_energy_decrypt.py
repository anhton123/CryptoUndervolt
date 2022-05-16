from Crypto.Cipher import AES
import time

NUM_OF_ITERATIONS = 20000
key = b'\x12\x34\x56\x78\x90\xab\xcd\xef\x12\x34\x56\x78\x90\xab\xcd\xef'
ciphertext = [210, 88, 80, 29]
tag = [254, 42, 116, 20, 50, 178, 182, 202, 10, 17, 59, 199, 109, 189, 52, 23]
nonce = [198, 253, 185, 96, 103, 174, 225, 58, 41, 87, 86, 36, 96, 234, 182, 83]

start = time.time()
for i in range(NUM_OF_ITERATIONS):
    cipher1 = AES.new(key, AES.MODE_GCM, nonce=bytes(nonce))                      
    plaintext = cipher1.decrypt_and_verify(bytes(ciphertext), bytes(tag))
    #print(plaintext)
end = time.time()
print(end-start)
