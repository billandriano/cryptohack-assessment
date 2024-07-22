import requests

def encrypt(plaintext):
    url = "https://aes.cryptohack.org/lazy_cbc/encrypt/"+plaintext
    request = requests.get(url)
    return request.json()["ciphertext"]

def get_flag(key):
    url = "https://aes.cryptohack.org/lazy_cbc/get_flag/"+key
    request = requests.get(url)
    return request.json()["plaintext"]

def receive(ciphertext):
    url = "https://aes.cryptohack.org/lazy_cbc/receive/"+ciphertext
    request = requests.get(url)
    return request.json()["error"][19:]

plaintext="756172656c617a79756172656c617a79756172656c617a79756172656c617a79" #hex of "uarelazyuarelazyuarelazyuarelazy"


ciphertext=encrypt(plaintext)

changed_ciphertext=ciphertext[:32]+"0"*32+ciphertext[:32]

invalid_plaintext=receive(changed_ciphertext)

key=hex(int(invalid_plaintext[:32],16)^int(invalid_plaintext[64:],16))

print(bytes.fromhex(get_flag(key[2:])))

