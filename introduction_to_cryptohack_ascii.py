

ascii_list_numbers=[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

ascii_string=""

for i in ascii_list_numbers:
    ascii_string+=chr(i)

print(ascii_string)
