import requests
import codecs


url = "https://aes.cryptohack.org/ecb_oracle/encrypt/"

#check bytes
"""for i in range(1,51):
    
    plaintext_test="A"*i
    plaintext_test_hex=plaintext_test.encode().hex()

    response = requests.get(url+plaintext_test_hex)
    response_json = response.json()['ciphertext']

    print(i,response_json)
"""

#we find the position

def find_same_blocks(response_json_list):
    for i in response_json_list:
        if response_json_list.count(i)>1:
            return i
    
''''
for i in range(0,50):
    
    plaintext_test="B"*i+"A"*32
    plaintext_test_hex=plaintext_test.encode().hex()

    response = requests.get(url+plaintext_test_hex)
    response_json = response.json()['ciphertext']
    response_json_list = str([response_json[i:i+32] for i in range(0, len(response_json), 32)])
    print(response_json_list)

    if find_same_blocks(response_json_list)!="'":
        print(find_same_blocks(response_json_list))
'''

def find_character(reference,found):
    
    for i in range(0, 255):
        plaintext_test="A"*(31-len(found))+found+chr(i)
        plaintext_test_hex=plaintext_test.encode().hex()

        response = requests.get(url+plaintext_test_hex)
        response_json = response.json()['ciphertext']    
        
        if reference==response_json[0:64]:
            return chr(i)
      
secret=''      
cnt=0

while secret=="" or secret[-1]!="}":
    
    plaintext_test="A"*(31-cnt)
   
    plaintext_test_hex=plaintext_test.encode().hex()

    response = requests.get(url+plaintext_test_hex)
    response_json = response.json()['ciphertext']
   
    found_character=find_character(response_json[0:64],secret)

    secret+=found_character
    cnt+=1
print(secret)
