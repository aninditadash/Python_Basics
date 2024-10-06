import hashlib

print(sorted(hashlib.algorithms_guaranteed))
print(sorted(hashlib.algorithms_available))

# It should be a python program which might read from a file on disk,
# We need to generate a secure hash of this code and detect if the code is later altered or modified
# as the hash generated will be different from the one originally generated
python_program = """
for i in range(10):
    print(i)
"""
print(python_program)

# encode function converts the unicode character to its integer representation, below using UTF-8 format
print(f"python_program.encode('utf8') \n{python_program.encode('utf8')}")

print("================================================================================")

for b in python_program.encode('utf8'):
    print(f"{b} = {chr(b)}")

original_hash = hashlib.sha256(python_program.encode('utf8'))

# hexdigest() method provides a hexadecimal representation of the secure hash
print(f"original_hash SHA256 hexdigest: {original_hash.hexdigest()}")

python_program += "    print('code change')"
print(python_program)

new_hash = hashlib.sha256(python_program.encode('utf8'))
print(f"new_hash SHA256 hexdigest: {new_hash.hexdigest()}")

if new_hash.hexdigest() == original_hash.hexdigest():
    print("The code has not been changed")
else:
    print("The code has been modified")

# Another use of secure hash is in version control systems (VCS). After initial upload of files to GitHub, if we
# are uploading modified versions of some files, VCS calculates the hash of all files and only uploads ones where
# new hash is different to the hash of the old version. Avoids uploading files unnecessarily and also the timestamp
# of the unmodified files remain unchanged.


