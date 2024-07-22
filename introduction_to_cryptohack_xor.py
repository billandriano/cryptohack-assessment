import string


given_string="label"
anwser=""
for i in given_string:
    
    anwser+=chr(ord(i)^13)
print(anwser)

    


    



