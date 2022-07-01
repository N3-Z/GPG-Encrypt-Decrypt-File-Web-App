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