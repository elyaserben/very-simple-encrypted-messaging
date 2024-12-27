import redis
import maskpass
import encrypt as dec


### ------------------- MAIN ----------------------------


print("encryption option:\n[1] Caesar Cipher\n[2] Vigenere Cipher\n[3] XOR Cipher")
enc_opt = maskpass.askpass(prompt="Please input decryption option (1, 2, 3, ...): ", mask="#")
dec.check_opt(enc_opt)

subscriber = redis.StrictRedis(host="localhost", port=6379, db=0)
channel = "my_channel"
pubsub = subscriber.pubsub()
pubsub.subscribe(channel)
print(f"Subscribed to {channel}. Waiting for message...")

for message in pubsub.listen():
    if message["type"] == "message":
        raw_message = message["data"].decode("utf-8")
        message = dec.crypt(raw_message, enc_opt, "dec")
        print(f">> {message}")
