import json
import os
import sys

urfile = input("enter path ur file :")
assert os.path.exists(urfile), "i  did not find the file at" + str(urfile)
#assert digunakan untuk melanjutkan eksekusi jika kondisi yang diberikan bernilai True. Jika kondisi penegasan bernilai False, maka akan memunculkan pengecualian AssertionError dengan pesan kesalahan yang ditentukan.
f = open(urfile, 'r+')
print("found the file!")
data = json.load(f)
print(data)
f.close()
