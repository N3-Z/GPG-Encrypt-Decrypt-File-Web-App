import gnu
# from shutil import which

g = gnu.GPG(gnupghome="/home/n3/.gnupg")
key_data = open('cert/user1/private.pgp').read()
import_result = g.import_keys(key_data,passphrase="12345678")
print(import_result)
print(import_result.fingerprints[0])
