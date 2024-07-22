from Crypto.Cipher import AES
import hashlib
import binascii


with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]

def decrypt(ciphertext_hex, words):

    for w in words:

        attempted_key = hashlib.md5(w.encode()).hexdigest()

        ciphertext = bytes.fromhex(ciphertext_hex)

        key=bytes.fromhex(attempted_key)
    
        cipher = AES.new(key, AES.MODE_ECB)
        
        decrypted = cipher.decrypt(ciphertext)
        try:
            result = binascii.unhexlify(decrypted.hex())
            
            if result.startswith('crypto{'.encode()):
                return result
                
        except:
            continue

print(decrypt("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66",words))