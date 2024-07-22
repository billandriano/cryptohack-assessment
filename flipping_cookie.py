from Crypto.Util.number import *
import requests

def getcookie():
    url = "https://aes.cryptohack.org/flipping_cookie/get_cookie/"
    request = requests.get(url)
    return request.json()["cookie"]

def getflag(cookie, iv):
    url = f"https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}"
    request = requests.get(url)
    return request.json()

cookie = getcookie()
print(f"Cookie: {cookie}")
print(f"iv : {cookie[:32]}")

iv = cookie[:32]

plaintext_b = b'admin=False;expi'
plaintext_a = b'admin=True;expir'

plaintext_b_hex = hex(bytes_to_long(plaintext_b))
plaintext_a_hex = hex(bytes_to_long(plaintext_a))

new_iv = hex(int(plaintext_b_hex, 16) ^ int(plaintext_a_hex, 16) ^ int(iv, 16))[2:]

print(f"New iv : {iv}")

print(getflag(cookie[32:], new_iv))
