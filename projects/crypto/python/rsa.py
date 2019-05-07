import base64
import os
import rsa


def load_priv_key(path):
    path = os.path.join(os.path.dirname(__file__), path)
    with open(path, mode='rb') as privatefile:
        keydata = privatefile.read()
    return rsa.PrivateKey.load_pkcs1(keydata)


def load_pub_key(path):
    path = os.path.join(os.path.dirname(__file__), path)
    with open(path, mode='rb') as pubfile:
        keydata = pubfile.read()
    return rsa.PublicKey.load_pkcs1(keydata)


def verify(message, signature, pubkey):
    signature = base64.b64decode(signature)
    return rsa.verify(message, signature, pubkey)


def sign(message, privkey):
    signature = rsa.sign(message, privkey, 'SHA-1')
    return base64.b64encode(signature)


def create_keys():
    (pubkey, privkey) = rsa.newkeys(512, True, 8)
    with open("id_rsa.pub", "w") as text_file:
        text_file.write(pubkey.save_pkcs1().decode('ascii'))
    with open("id_rsa", "w") as text_file:
        text_file.write(privkey.save_pkcs1().decode('ascii'))
