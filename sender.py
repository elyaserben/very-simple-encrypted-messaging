import redis
import maskpass
import encrypt as enc


### ------------------- MAIN ----------------------------


print("encryption option:\n[1] Caesar Cipher\n[2] Vigenere Cipher")
enc_opt = maskpass.askpass(prompt="Please input encryption option (1, 2, 3, ...): ", mask="#")
enc.check_opt(enc_opt)

print("Enter message (no numerical or special characters allowed): ")

publisher = redis.StrictRedis(host="localhost", port=6379, db=0)
channel = "my_channel"
while True:
    raw_message = input(">> ")
    message = enc.crypt(raw_message, enc_opt, "enc")
    publisher.publish(channel, message)