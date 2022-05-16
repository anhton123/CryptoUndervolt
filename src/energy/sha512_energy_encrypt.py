from Crypto.Hash import SHA512
import time

NUM_OF_ITERATIONS = 300000
plaintext = b"\xab\xcd\xef\x12"

start = time.time()
for i in range(NUM_OF_ITERATIONS):
    h = SHA512.new()
    h.update(plaintext)
    #print(h.hexdigest())
end = time.time()
print(end-start)
    
