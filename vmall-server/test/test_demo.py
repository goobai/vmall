import random
import os
import datetime

# SALT_CHARS = "1234567890"
#
#
# def gen_salt(length):
#     """Generate a random string of SALT_CHARS with specified ``length``."""
#     if length <= 0:
#         raise ValueError("Salt length must be positive")
#     return "".join(random.choice(SALT_CHARS) for _ in range(length))
#
#
# print('.............')
# b = gen_salt(4)
# a = os.listdir('.')
# print(a)
# a = os.path.abspath('g:/pyenv')
x = lambda x: x * 2
a = map(x, [1, 2, 3, 4, 5])
print(a)
for key in a:
    print(key)
