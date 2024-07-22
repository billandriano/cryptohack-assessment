def xor_bytes(bytes1, bytes2):
    return bytes(x ^ y for x, y in zip(bytes1, bytes2))

enc_msg = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

dec_msg = 'crypto{'

key = xor_bytes(enc_msg[:8], dec_msg[:8].encode('utf-8'))
key = key.decode('utf-8')+'y'

#key='myXORke'+'y'

pos_dec_msg = xor_bytes(key.encode('utf-8'), enc_msg)

cnt = 0
new_key = key

while chr(pos_dec_msg[-1]) != '}':

    new_key += key[cnt % 8]  # Modified to cycle through the key more efficiently

    pos_dec_msg = xor_bytes(new_key.encode('utf-8'), enc_msg)
    cnt += 1

print(pos_dec_msg)
