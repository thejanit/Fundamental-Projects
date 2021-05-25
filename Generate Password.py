import random
import string

str_lower = string.ascii_lowercase
str_upper = string.ascii_uppercase
str_num = string.digits
str_punc = string.punctuation

passwd_len = int(input('Enter the length of password: '))

s = []
s.extend(list(str_lower))
s.extend(list(str_upper))
s.extend(list(str_num))
s.extend(list(str_punc))

p = "".join(random.sample(s, passwd_len))
print(p)