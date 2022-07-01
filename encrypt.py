import gnu
gpg = gnu.GPG(gnupghome="/home/n3/.gnupg")

# gpg = gnupg.GPG(homedir="/home/n3/.gnupg")
# gpg._encoding = 'utf-8'
# print(gpg.keyring)
# print(gpg.list_keys(True))
with open('testing_encrypt_user1.txt', 'rb') as f:
    status = gpg.encrypt_file(
        f, recipients=["C519930C4A6893FE0DF62F764C321CEEA5C8B310"],
        output='output.gpg', always_trust=True
    )
    

print("ok\t\t: "+  str(status.ok))
print("status\t: "+str(status.status))
print("stderr\t: "+str(status.stderr))


# https://zhou-en.github.io/2020/10/21/Encrypt-and-Decrypt-File-with-python-gnupg/
# https://matduggan.com/til-easy-way-to-encrypt-and-decrypt-files-with-python-and-gpg/

# Python 3.10.4 (main, Mar 24 2022, 13:07:27) [GCC 11.2.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import gnupg
# >>>
# >>> g = gnupg.GPG(homedir="/home/n3/.gnupg")
# >>> key_data = open('xavani_public.key').read()
# >>> import_result = g.import_keys(key_data)
# >>> print(import_result.results)
# [{'fingerprint': '458BF11A698F4CB71EADAF3BAFD36537A225AD5F', 'status': 'Not actually changed\n'}, {'status': 'key considered'}]
# >>> key_data = open('xavani_public.key').read()
# >>> import_result = g.import_keys(key_data)
# >>> print(import_result.results)
# [{'status': 'key considered'}, {'fingerprint': '458BF11A698F4CB71EADAF3BAFD36537A225AD5F', 'status': 'Entirely new key\n'}]
# >>> print(import_result.key_data)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'ImportResult' object has no attribute 'key_data'
# >>> print(import_result.fingerprints)
# ['458BF11A698F4CB71EADAF3BAFD36537A225AD5F']
# >>> print(import_result.fingerprints[0])
# 458BF11A698F4CB71EADAF3BAFD36537A225AD5F
# >>> x = "Hello World"
# >>> key = import_result.fingerprints[0]
# >>> encrypted = str(g.encrypt(x, key))
# Exception in thread Thread-8 (_read_response):
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/threading.py", line 1009, in _bootstrap_inner
#     self.run()
#   File "/usr/lib/python3.10/threading.py", line 946, in run
#     self._target(*self._args, **self._kwargs)
#   File "/home/n3/.local/lib/python3.10/site-packages/gnupg/_meta.py", line 650, in _read_response
#     result._handle_status(keyword, value)
#   File "/home/n3/.local/lib/python3.10/site-packages/gnupg/_parsers.py", line 1757, in _handle_status
#     super(Crypt, self)._handle_status(key, value)
#   File "/home/n3/.local/lib/python3.10/site-packages/gnupg/_parsers.py", line 1656, in _handle_status
#     raise ValueError("Unknown status message: %r" % key)
# ValueError: Unknown status message: 'ENCRYPTION_COMPLIANCE_MODE'
# >>> g.encrypt(x,key)
# Exception in thread Thread-11 (_read_response):
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/threading.py", line 1009, in _bootstrap_inner
#     self.run()
#   File "/usr/lib/python3.10/threading.py", line 946, in run
#     self._target(*self._args, **self._kwargs)
#   File "/home/n3/.local/lib/python3.10/site-packages/gnupg/_meta.py", line 650, in _read_response
#     result._handle_status(keyword, value)
#   File "/home/n3/.local/lib/python3.10/site-packages/gnupg/_parsers.py", line 1757, in _handle_status
#     super(Crypt, self)._handle_status(key, value)
#   File "/home/n3/.local/lib/python3.10/site-packages/gnupg/_parsers.py", line 1656, in _handle_status
#     raise ValueError("Unknown status message: %r" % key)
# ValueError: Unknown status message: 'ENCRYPTION_COMPLIANCE_MODE'
# <gnupg._parsers.Crypt object at 0x7fdb486f0df0>
# >>> g.search('xavani.ao@gmail.com')~
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'GPG' object has no attribute 'search'
# >>> g.search_keys('xavani.ao@gmail.com')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'GPG' object has no attribute 'search_keys'. Did you mean: '_parse_keys'?
# >>> g.encrypt(x,'xavani.ao@gmail.com')
# <gnupg._parsers.Crypt object at 0x7fdb48732890>
# >>> str(g.encrypt(x,'xavani.ao@gmail.com'))
# ''
# >>> x
# 'Hello World'
# >>> g.search_keys('xavani.ao@gmail.com')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'GPG' object has no attribute 'search_keys'. Did you mean: '_parse_keys'?