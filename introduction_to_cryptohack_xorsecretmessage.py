def xor_bytes(bytes1, bytes2):
    return bytes(x ^ y for x, y in zip(bytes1, bytes2))

secret = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

msg = ''

ascii_chrs = ''.join(chr(i) for i in range(128))

for b in ascii_chrs.encode('utf-8'):
    for i in secret:
        msg += chr(xor_bytes(bytes([b]), bytes([i]))[0])
    print(msg)
    msg = ""
