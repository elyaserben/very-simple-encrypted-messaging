import string
import maskpass


### ------------------- ADDITIONAL INPUT ----------------------------


def check_opt(enc_opt):
    match enc_opt:  
        case "1": 
            global shift
            shift = int(maskpass.askpass(prompt="Shift key: ", mask="#"))
        case "2":
            global raw_key1
            raw_key1 = maskpass.askpass(prompt="Key: ", mask="#")
        case "3":
            global raw_key2
            raw_key2 = maskpass.askpass(prompt="Key: ", mask="#")
        case _:
            print("Wrong option")


### ------------------- ENCRYPT/DECRYPT ----------------------------


def crypt(raw_message, enc_opt, enc_dec):
    match enc_opt:
        case "1":
            message = "".join(caesar_cipher(raw_message, shift, enc_dec))
            return message
        case "2":
            message = "".join(vigenere_cipher(raw_message, raw_key1, enc_dec))
            return message
        case "3":
            message = xor_cipher(raw_message, raw_key2)
            return message
        case _:
            print("Wrong option")


### ------------------- KEY CONDITIONER ----------------------------


def key_conditioner(raw_key, length):
    return (raw_key * (length//len(raw_key) + 1))[:length].lower()


### ------------------- CAESAR ----------------------------


def caesar_cipher(raw_message, shift, enc_dec):
    base = string.ascii_lowercase
    key = base[-shift:]+base[:-shift]
    message = "".join(e for e in raw_message if e.isalpha()).lower()

    new_message = []

    match enc_dec:
        case "enc":
            for i in range(len(message)):
                for j in range(len(base)):
                    if message[i] == base[j]:
                        new_message.append(key[j])
        case "dec":
            for i in range(len(message)):
                for j in range(len(base)):
                    if message[i] == key[j]:
                        new_message.append(base[j])   

    return new_message


### ------------------- VIGENERE ----------------------------


def vigenere_cipher(raw_message, raw_key, enc_dec):
    base = string.ascii_lowercase * 2
    message = "".join(e for e in raw_message if e.isalpha()).lower()
    key = key_conditioner(raw_key, len(message))

    new_message = []
    
    match enc_dec:
        case "enc":
            for i in range (len(message)):
                index = string.ascii_lowercase.index(message[i]) + string.ascii_lowercase.index(key[i]) % 26
                new_message.append(base[index])
        case "dec":
            for i in range (len(message)):
                index = string.ascii_lowercase.index(message[i]) - string.ascii_lowercase.index(key[i]) % 26
                new_message.append(base[index])

    return new_message


### ------------------- XOR ----------------------------


def xor_cipher(message, raw_key):
    message = bytearray(message, 'utf-8')
    key = bytearray(key_conditioner(raw_key, len(message)), 'utf-8')

    new_message = bytearray(len(message))

    for i in range(len(message)):
        new_message[i] = message[i] ^ key[i]
    
    return new_message.decode('utf-8')
