import requests
from pwn import xor



def decrypt(ciphertext):
    url = "https://aes.cryptohack.org/ecbcbcwtf/decrypt/"
    response = requests.get(url+ciphertext)
    response_json = response.json()['plaintext']

    return response_json

def main():
    ciphertext_iv="a42488d0ca4c29bcd7fb313ede555f810d693be62af32a237691610be8f0a40295d8f42c88575422f445eaaf29ddb7b3"

    iv=bytes.fromhex(ciphertext_iv[0:32])

    ciphertext_1st_block=ciphertext_iv[32:64]
    ciphertext_2nd_block=ciphertext_iv[64:]

    plaintext_1st_block=bytes.fromhex(decrypt(ciphertext_1st_block))
    plaintext_2nd_block=bytes.fromhex(decrypt(ciphertext_2nd_block))

    return xor(iv,plaintext_1st_block).decode() + xor(bytes.fromhex(ciphertext_1st_block),plaintext_2nd_block).decode()


print(main())








