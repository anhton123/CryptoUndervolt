from Crypto.Hash import SHA256
import time

NUM_OF_ITERATIONS = 200000
plaintext = b"\xab\xcd\xef\x12"

start = time.time()
for i in range(NUM_OF_ITERATIONS):
    h = SHA256.new()
    h.update(plaintext)
    #print(h.hexdigest())
end = time.time()
print(end-start)
