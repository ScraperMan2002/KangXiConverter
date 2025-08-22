import re


with open('KangXi.txt', 'r') as file:
    str_kang_xi = file.read()

with open('source.txt', 'r') as file:
    str_source = file.read()

str_kang_xi_list = str_kang_xi.split('\n')
for str_chars in str_kang_xi_list:
    str_source = re.sub(str_chars[0], str_chars[1], str_source)
with open('source.txt', 'w') as file:
    file.write(str_source)
