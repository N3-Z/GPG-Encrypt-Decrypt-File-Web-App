import gnu


gpg = gnu.GPG(gnupghome="/home/n3/.gnupg")
with open('teesting_decrypt_user2.txt', 'rb') as f:
    status = gpg.decrypt_file(
        f,
        output='plaintext_output.text',
        passphrase="12345678"
    )

print("ok\t\t: "+  str(status.ok))
print("status\t: "+str(status.status))
print("stderr\t: "+str(status.stderr))