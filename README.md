# encrypt
gpg
gpg --encrypt -r email my-unencrypted.txt


# decrypt
gpg --import private.pgp
gpg -d my-unencrypted.txt.asc > output.txt

# command
python2 main.py --public cert/User1/public.key --private cert/User2/private.pgp --passphrase 12345678
atau
python3 main.py --public cert/User1/public.key --private cert/User2/private.pgp --passphrase 12345678


# Tools requirement
- gpg (GnuPG) 2.2.35
- Python 2.7.18 (Support)
- Python 3.10.5 (Support)

# Python library requirements
- flask
- argparse
