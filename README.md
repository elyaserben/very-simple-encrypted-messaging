# very-simple-encrypted-messaging
Simple encrypted messaging

## setup:
- docker desktop must be installed
- my python version is 3.12.8
- run: docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
- run: pip install maskpass
- run: pip install redis
- open redis insight (localhost:8001):
  - accept recommended option and terms & agreements, next
  - go to pub/sub
  - click subscribe

## caesar cipher:
1. open terminal, run: python sender.py
2. open another terminal, run: python receiver.py
3. in sender, for example:
   - encryption option: 1
   - key: 3
4. in receiver, use appropriate decryption option:
   - decryption option: 1
   - key: 3
5. in sender, for example:
   >> Attack at dawn!
6. in receiver we will get:
   >> attackatdawn

![image](https://github.com/user-attachments/assets/0babc786-10bb-42ef-b326-c7ee92255e6c)
7. in redis insight, we will get:
    ![image](https://github.com/user-attachments/assets/a585c7a9-67fc-43c1-be88-1089e70f8fa6)
8. explanation:
   - "Attack at dawn!" will be filtered into "attackatdawn" (only alphabetical character)
   - base = string.ascii_lowercase is generating 'abcdefghijklmnopqrstuvwxyz'
   - key = base, but rotated with shift
   - if shift = 3, then key = 'xyzabcdefghijklmnopqrstuvw'
   - now compare it:
     - abcdefghijklmnopqrstuvwxyz
     - xyzabcdefghijklmnopqrstuvw
     - a become x, z become w, and so on
   - so, attackatdawn = xqqxzhxqaxtk

## vigenere cipher:
1. open terminal, run: python sender.py
2. open another terminal, run: python receiver.py
3. in sender, for example:
   - encryption option: 2
   - key: lemon
4. in receiver, use appropriate decryption option:
   - decryption option: 2
   - key: lemon
5. in sender, for example:
   >> Attack at dawn!
6. in receiver we will get:
   >> attackatdawn

![image](https://github.com/user-attachments/assets/a707b0db-6cfa-4cf8-8f6f-fbbe85ffec2c)
7. in redis insight, we will get:
    ![image](https://github.com/user-attachments/assets/c7883834-75b7-4e7b-8314-d1b65a999e38)
8. explanation:
   - "Attack at dawn!" will be filtered into "attackatdawn" (only alphabetical character)
   - key = lemon
   - key will be extended (by repeating it) or trimmed in respect to the length of filtered message
   - length of "attackatdawn" is 12, so the key will become "lemonlemonle"
   - if key is "whateveryouwant" then it will become "whateveryouw"
   - encrypt:
      ![image](https://github.com/user-attachments/assets/9eda28e8-eeef-4921-8fd8-0e0a85ccd133)
   - so, we iterate through every character in "attackatdawn" and the key
     - attackatdawn
     - lemonlemonle
     - alphabet has 26 characters, the index for it is 0-25
     - iteration 1:
       - what is the index for "a" in the alphabet? it is 0
       - what is the index for "l" in the alphabet? it is 11
       - so, (0 + 11) % 26 = 11 --> l
     - iteration 2:
       - what is the index for "t" in the alphabet? it is 19
       - what is the index for "e" in the alphabet? it is 4
       - so, (19 + 4) % 26 = 23 --> x
     - iteration 3:
       - what is the index for "t" in the alphabet? it is 19
       - what is the index for "m" in the alphabet? it is 12
       - so, (19 + 12) % 26 = 5 --> f
     - repeat it until we got the encrypted message "lxfopvefrnhr" (you can see it in the redis insight)
   - decrypt:
      ![image](https://github.com/user-attachments/assets/8fd86e0d-3ecc-4dc2-ae1c-0c15a0dc02cd)
   - so, we iterate through every character in "lxfopvefrnhr" and the key
     - lxfopvefrnhr
     - lemonlemonle
     - iteration 1:
       - what is the index for "l" in the alphabet? it is 11
       - what is the index for "l" in the alphabet? it is 11
       - so, (11 - 11) % 26 = 0 --> a
     - iteration 2:
       - what is the index for "x" in the alphabet? it is 23
       - what is the index for "e" in the alphabet? it is 4
       - so, (23 - 4) % 26 = 19 --> t
     - iteration 3:
       - what is the index for "f" in the alphabet? it is 5
       - what is the index for "m" in the alphabet? it is 12
       - so, (5 - 12) % 26 = 19 --> t
     - repeat it until we got the decrypted message "attackatdawn"
     
## XOR cipher:
1. open terminal, run: python sender.py
2. open another terminal, run: python receiver.py
3. in sender, for example:
   - encryption option: 3
   - key: lemon
4. in receiver, use appropriate decryption option:
   - decryption option: 3
   - key: lemon
5. in sender, for example:
   >> Attack at dawn!
6. in receiver we will get:
   >> Attack at dawn!

![image](https://github.com/user-attachments/assets/63f38b8f-2023-4d76-b5a0-2f46ee59e6c5)
7. in redis insight, we will get:
    ![image](https://github.com/user-attachments/assets/1ebf1c30-50bc-44c1-a217-b3e35b76a9c0)
8. explanation:
   - length of "Attack at dawn!" is 15 characters, so the key will become "lemonlemonlemon"
   - see https://en.wikipedia.org/wiki/List_of_Unicode_characters
   - example 1:
     - message[0] -> A = 65 = 01000001
     - key[0] -> l = 108 = 01101100
     - encrypted_message = message XOR key = 01000001 XOR 01101100 = 00101101 = 45 = hyphen-minus (-)
     - decrypted_message = encrypted_message XOR key = 00101101 XOR 01101100 = 01000001 = 65 = A
   - example 2:
     - message[14] -> ! = 33 = 00100001
     - key[14] -> n = 110 = 01101110
     - encrypted_message = message XOR key = 00100001 XOR 01101110 = 01001111 = 79 = O
     - decrypted_message = encrypted_message XOR key = 01001111 XOR 01101110 = 00100001 = 33 = !



