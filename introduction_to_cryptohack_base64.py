
import base64

hex_string="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

#We decode first to bytes with bytes.fromhex and then we encode with base64.b64encode

print(base64.b64encode(bytes.fromhex(hex_string)))
