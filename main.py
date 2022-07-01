from flask import Flask, render_template, request, send_file
# import gnupg
import argparse

import gnu


api = Flask(__name__)
api.config['DEBUG'] = True

# Edit gnupghome
gpg = gnu.GPG(gnupghome="/home/n3/.gnupg")
PASSPHRASE = ""
PUBLICKEY_ID = ""
PRIVATEKEY_ID = ""

parser = argparse.ArgumentParser()
parser.add_argument("--public", help="Path public key")
parser.add_argument("--private",help="Path private key")
parser.add_argument("--passphrase",help="Passphrase private key")
parser.add_argument("Example:",help="python3 main.py --public [public key path] --private [private key path] --passphrase [passphrase]")


@api.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@api.route('/upload', methods=['GET','POST'])
def upload():
    global PRIVATEKEY_ID
    global PUBLICKEY_ID
    global PASSPHRASE
    if request.method == 'POST':
        file = request.files['file']
        
        upload_type = request.form['type']
        pathOutput = "output_file/" + str(file.filename)
        status = None
        if upload_type == "encrypt":
            status = gpg.encrypt_file(
                file, recipients=[PUBLICKEY_ID],
                output=pathOutput, always_trust=True
            )
        elif upload_type == "decrypt":
            status = gpg.decrypt_file(
                file,
                output=pathOutput,
                passphrase=PASSPHRASE,
                always_trust=True
            )
            print("ok\t\t: "+  str(status.ok))
            print("status\t: "+str(status.status))
            print("stderr\t: "+str(status.stderr))
        return send_file(pathOutput, as_attachment=True)
    elif request.method == 'GET':
        return 'Upload file!' 

def import_key():
    global PASSPHRASE
    global PUBLICKEY_ID
    global PRIVATEKEY_ID
    args = parser.parse_args()
    PASSPHRASE = args.passphrase
    public_key_path = args.public
    private_key_path = args.private

    public_key_data = open(public_key_path).read()
    private_key_data = open(private_key_path).read()

    PUBLICKEY_ID = gpg.import_keys(public_key_data).fingerprints[0]
    PRIVATEKEY_ID = gpg.import_keys(private_key_data).fingerprints[0]


def main():
    import_key()
    api.run()

if __name__ == '__main__':
    main()