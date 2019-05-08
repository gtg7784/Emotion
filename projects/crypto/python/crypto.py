"""
/*********************************************************************
* Filename:     crypto.c
* Author:       EMOTION the artificial intelligence club of sunrin internet high school
* Copyright:    GNU GENERAL PUBLIC LICENSE
* Disclaimer:   This code is base64, url, sha256, md5, rsa en/decoder
* Details:      Performs known-answer tests on the corresponding AES
                implementation. These tests do not encompass the full
                range of available test vectors and are not sufficient
                for FIPS-140 certification. However, if the tests pass
                it is very, very likely that the code is correct and was
                compiled properly. This code also serves as
                example usage of the functions.
*********************************************************************/


/*********************************************************************
 * Type: base64
 * Role: 이다은
 * Principle: base64는 문자열을 입력받아 8bit의 데이터를 6bit로 표기
*********************************************************************/


/*********************************************************************
 * Type: sha256
 * Role: 10101 김재현
 * Principle: 
*********************************************************************/


/*********************************************************************
 * Type: md5
 * Role: 10411 박민준
 * Principle: 
*********************************************************************/


/*********************************************************************
 * Type: url, rsa
 * Role: 고태건
 * Principle: 
*********************************************************************/
"""

import base64
import hashlib
import urllib.parse

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib

def printEmotion():
    print("                                                ,----,                                    ")
    print("                    ____      ,----..         ,/   .`|            ,----..            ,--. ")
    print("    ,---,.        ,'  , `.   /   /   \\      ,`   .'  :   ,---,   /   /   \\         ,--.'| ")
    print("  ,'  .' |     ,-+-,.' _ |  /   .     :            /,`--.' |  /   .     :    ,--,:  : | ")
    print(",---.'   |  ,-+-.    , || .   /   .  \\.'___,/    ,' |   :  : .   /   .  \\,`--.'`|  ' : ")
    print("|   |   .' ,--.'|'   |  |.      /  ` |    :     |  :   |  '.      /  ` |   :  :  | | ")
    print(":   :  |-,|   |  ,', |  ':   |   \\  |    |.'    |   :  |   |   \\  |:   |   \\ | : ")
    print(":   |  /||   | /  | |  |||   :  |  | '`----'  |  |  '   '  |   :  |  | '|   : '  ' | ")
    print("|   :   .''   | :  | :  |,.   |  ' ' ' :    '   :    |   |  |.   |  ' ' ' :'   ' .     ")
    print("|   |  |-,   . |   |--' '     \\ /  |    |   |  '  '   :  '     \\ /  ||   | | \\   | ")
    print("'   :  /||   : |  | ,     \\   \\  ',  /     '   :  |  |   |  ' \\   \\  ',  / '   : |   .' ")
    print("|   |    \\|   : '  |/          :    /         |.'   '   :  |     :    /  |   | '`--'   ")
    print("|   :   .'   | |`-'         \\   \\ .'       '---'        |.'    \\   \\ .'   '   : |       ")
    print("|   | ,'  |   /              `---`                   '---'       `---`        |.'       ")
    print("`----'    '---'                                                             '---'         ")

def printCrypto():
    print("                                                        ,----,             ")
    print("                                     ,-.----.         ,/   .`|  ,----..    ")
    print("      ,----..  ,-.----.              \\    /  \\      ,`   .'  : /   /   \\   ")
    print("     /   /   \\ \\    /  \\        ,---,|   :    \\            //   .     :  ")
    print("    |   :     :   :    \\      /_ ./||   |  .\\ :.'___,/    ,'.   /   .  \\ ")
    print("    .   |  . /|   | .\\ :,---, |  ' :.   :  |: ||    :     |.      /  `  ")
    print("    .    /--` .   : |: /___/ \\.  : ||   |   \\ :    |.'     |   \\  | ")
    print("       |     |   |  \\ :.  \\  \\ ,' '|   : .   /`----'  |  ||   :  |  | ' ")
    print("    |   : |    |   : .  / \\    `  ,'   | |`-'     '   :  .   |  ' ' ' : ")
    print("    .   | '___    | |  \\  \\  \\    ' |   |         |   |  ''     \\ /  | ")
    print("    '    : .'||   | \\  \\  '  \\   | :   ' |        '   :  | \\   \\  ',  /  ")
    print("    '   | '/  ::   ' | \\.'   \\     :   : :           |.'      :    /   ")
    print("    |   :    / :   : :-'      :  \\  \\|   | :        '---'      \\   \\ .'    ")
    print("    \\   \\ .'  |   |.'         \\  ' `---'.|                    `---`      ")
    print("    `---`    `---'            `--`   `---`                   ")

def printEndecode():
    print("                                                                                                                      ")
    print("                   ,--.                                                  ,----..                                      ")
    print("    ,---,.       ,--.'|        ,--,    ,---,        ,---,.  ,----..     /   /   \\      ,---,        ,---,.,-.----.    ")
    print("  ,'  .' |   ,--,:  : |       / .`|  .'  .' `\\    ,'  .' | /   /   \\   /   .     :   .'  .' `\\    ,'  .' |\\    /  \\   ")
    print(",---.'   |,`--.'`|  ' :      /' / ,---.'     \\ ,---.'   ||   :     : .   /   .  \\,---.'     \\ ,---.'   |   :    \\  ")
    print("|   |   .'|   :  :  | |     /  / .'|   |  .`\\  ||   |   .'.   |  . /.      /  ` |   |  .`\\  ||   |   .'|   | .\\ :  ")
    print(":   :  |-,:   |   \\ | :    /  / ./ :   : |  '  |:   :  |-,.    /--`    |   \\  |:   : |  '  |:   :  |-,.   : |: |  ")
    print(":   |  /||   : '  ' |   / ./  /  |   ' '    ::   |  /|   |     |   :  |  | '|   ' '    ::   |  /||   |  \\ :  ")
    print("|   :   .''   ' .      /  /  /   '   |   .  ||   :   .'|   : |    .   |  ' ' ' :'   |   .  ||   :   .'|   : .  /  ")
    print("|   |  |-,|   | | \\   | /  /  /    |   | :  |  '|   |  |-,.   | '___ '     \\ /  ||   | :  |  '|   |  |-,   | |  \\  ")
    print("'   :  /|'   : |   .'  /  /     '   : | /   '   :  /|'    : .'| \\   \\  ',  / '   : | /   '   :  /||   | \\  \\ ")
    print("|   |    \\|   | '`--'./__  /      |   | '` ,/  |   |    \\'   | '/  :     :    /  |   | '` ,/  |   |    \\:   ' | \\.' ")
    print("|   :   .''   : |    |   : /          :  .'    |   :   .'|   :    /    \\   \\ .'      :  .'    |   :   .':   : :-'   ")
    print("|   | ,'     |.'       |/        |   ,.'      |   | ,'   \\   \\ .'      `---`     |   ,.'      |   | ,'  |   |.'     ")
    print("`----'    '---'      `---'         '---'        `----'      `---`                  '---'        `----'    `---'       ")

def printEncode():
    print("                                                                                       ")
    print("                   ,--.               ,----..                                      ")
    print("    ,---,.       ,--.'|  ,----..     /   /   \\      ,---,        ,---,.,-.----.    ")
    print("  ,'  .' |   ,--,:  : | /   /   \\   /   .     :   .'  .' `\\    ,'  .' |\\    /  \\   ")
    print(",---.'   |,`--.'`|  ' :|   :     : .   /   .  \\,---.'     \\ ,---.'   |   :    \\  ")
    print("|   |   .'|   :  :  | |.   |  . /.      /  ` |   |  .`\\  ||   |   .'|   | .\\ :  ")
    print(":   :  |-,:   |   \\ | :.    /--`    |   \\  |:   : |  '  |:   :  |-,.   : |: |  ")
    print(":   |  /||   : '  ' |   |     |   :  |  | '|   ' '    ::   |  /||   |  \\ :  ")
    print("|   :   .''   ' .    |   : |    .   |  ' ' ' :'   |   .  ||   :   .'|   : .  /  ")
    print("|   |  |-,|   | | \\   |.   | '___ '     \\ /  ||   | :  |  '|   |  |-,   | |  \\  ")
    print("'   :  /|'   : |   .''    : .'| \\   \\  ',  / '   : | /   '   :  /||   | \\  \\ ")
    print("|   |    \\|   | '`--'  '   | '/  :     :    /  |   | '` ,/  |   |    \\:   ' | \\.' ")
    print("|   :   .''   : |      |   :    /    \\   \\ .'      :  .'    |   :   .':   : :-'   ")
    print("|   | ,'     |.'       \\   \\ .'      `---`     |   ,.'      |   | ,'  |   |.'     ")
    print("`----'    '---'          `---`                  '---'        `----'    `---'       ")

def printDecode():
    print("                                                                                       ")
    print("                                      ,----..                                      ")
    print("    ,---,        ,---,.  ,----..     /   /   \\      ,---,        ,---,.,-.----.    ")
    print("  .'  .' `\\    ,'  .' | /   /   \\   /   .     :   .'  .' `\\    ,'  .' |\\    /  \\   ")
    print(",---.'     \\ ,---.'   ||   :     : .   /   .  \\,---.'     \\ ,---.'   |   :    \\  ")
    print("|   |  .`\\  ||   |   .'.   |  . /.      /  ` |   |  .`\\  ||   |   .'|   | .\\ :  ")
    print(":   : |  '  |:   :  |-,.    /--`    |   \\  |:   : |  '  |:   :  |-,.   : |: |  ")
    print("|   ' '    ::   |  /|   |     |   :  |  | '|   ' '    ::   |  /||   |  \\ :  ")
    print("'   |   .  ||   :   .'|   : |    .   |  ' ' ' :'   |   .  ||   :   .'|   : .  /  ")
    print("|   | :  |  '|   |  |-,.   | '___ '     \\ /  ||   | :  |  '|   |  |-,   | |  \\  ")
    print("'   : | /   '   :  /|'    : .'| \\   \\  ',  / '   : | /   '   :  /||   | \\  \\ ")
    print("|   | '` ,/  |   |    \\'   | '/  :     :    /  |   | '` ,/  |   |    \\:   ' | \\.' ")
    print("       :  .'    |   :   .'|   :    /    \\   \\ .'      :  .'    |   :   .':   : :-'   ")
    print("|   ,.'      |   | ,'   \\   \\ .'      `---`     |   ,.'      |   | ,'  |   |.'     ")
    print("'---'        `----'      `---`                  '---'        `----'    `---'       ")

def generateKey():
    #Generate a public/ private key pair using 4096 bits key length (512 bytes)
    new_key = RSA.generate(4096, e=65537)

    #The private key in PEM format
    private_key = new_key.exportKey("PEM")

    #The public key in PEM Format
    public_key = new_key.publickey().exportKey("PEM")

    print(private_key)
    fd = open("private_key.pem", "wb")
    fd.write(private_key)
    fd.close()

    print(public_key)
    fd = open("public_key.pem", "wb")
    fd.write("public key is ", public_key)
    fd.close()


def encrypt_rsa(blob, public_key):
    #Import the Public Key and use for encryption using PKCS1_OAEP
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    #compress the data first
    blob = zlib.compress(blob)

    #In determining the chunk size, determine the private key length used in bytes
    #and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    #in chunks
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted =  ""

    while not end_loop:
        #The chunk
        chunk = blob[offset:offset + chunk_size]

        #If the data chunk is less then the chunk size, then we need to add
        #padding with " ". This indicates the we reached the end of the file
        #so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += " " * (chunk_size - len(chunk))

        #Append the encrypted chunk to the overall encrypted file
        encrypted += rsa_key.encrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #Base 64 encode the encrypted file
    return base64.b64encode(encrypted)

def decrypt_rsa(encrypted_blob, private_key):

    #Import the Private Key and use for decryption using PKCS1_OAEP
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    #Base 64 decode the data
    encrypted_blob = base64.b64decode(encrypted_blob)

    #In determining the chunk size, determine the private key length used in bytes.
    #The data will be in decrypted in chunks
    chunk_size = 512
    offset = 0
    decrypted = ""

    #keep loop going as long as we have chunks to decrypt
    while offset < len(encrypted_blob):
        #The chunk
        chunk = encrypted_blob[offset: offset + chunk_size]

        #Append the decrypted chunk to the overall decrypted file
        decrypted += rsakey.decrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #return the decompressed decrypted data
    return zlib.decompress(decrypted)

def base(cyptotype):
    if (cyptotype == 1):
        inp = input("Type you want to encode: ")
        a = inp.encode("utf-8")
        b = base64.b64encode(a)
        outp = b.decode("utf-8")
        print(outp)
    elif (cyptotype == 2):
        inp = input("Type you want to decode: ")
        a = inp.encode("utf-8")
        b = base64.b64decode(a)
        outp = b.decode("utf-8")
        print(outp)

def url(cyptotype):
    if (cyptotype == 1):
        inp = input("Type you want to encode: ")
        a = inp.encode("utf-8")
        outp = urllib.parse.quote(a)
        print(outp)
    elif (cyptotype == 2):
        inp = input("Type you want to encode: ")
        a = inp.encode("utf-8")
        outp = urllib.parse.unquote(a)
        print(outp)
    
def rsa(cyptotype):
    if (cyptotype == 1):
        inp = input("Type you want to encode: ")
        unencrypted_blob = inp.encode("utf-8")

        generateKey()

        fd = open("public_key.pem", "rb")
        public_key = fd.read()
        fd.close()

        encrypted_blob = encrypt_rsa(unencrypted_blob, public_key)

        fd = open("encrypted.txt", "wb")
        fd.write(encrypted_blob.encode('utf-8'))
        fd.close()


    elif (cyptotype == 2):  
        inp = input("Type you want to encode: ")
        a = inp.encode("utf-8")

        fd = open("private_key.pem", "rb")
        private_key = fd.read()
        fd.close()

        #Our candidate file to be decrypted
        fd = open("encrypted.txt", "rb")
        encrypted_blob = fd.read()
        fd.close()

        #Write the decrypted contents to a file
        fd = open("decrypted.txt", "wb")
        fd.write(decrypt_rsa(encrypted_blob, private_key))
        fd.close()

        

def sha256():
    inp = input("Type you want to hash: ")
    a = inp.encode("utf-8")
    sha = hashlib.new('sha256')
    sha.update(a)
    print(sha.hexdigest())

def md5():
    inp = input("Type you want to hash: ")
    a = inp.encode("utf-8")
    sha = hashlib.new('md5')
    sha.update(a)
    print(sha.hexdigest())

def encode():
    printEncode()
                                                                                                                      
    print("Select the number…")
    print("1. BASE64")
    print("2. URL")
    print("3. SHA256")
    print("4. MD5")
    print("5. RSA")
    print("ANY OHTER NUMBER TO EXIT...")

    menu = int(input("> "))

    if (menu == 1):
        base(1)
    elif (menu == 2):
        url(1)
    elif (menu == 3):
        sha256()
    elif (menu == 4):
        md5()
    elif (menu == 5):
        rsa(1)
    else:
        print("EXIT... BYEBYE")


def decode():
    printDecode()
    print("Select the number…")
    print("1. BASE64")
    print("2. URL")
    print("3. RSA")
    print("ANY OHTER NUMBER TO EXIT...")
    menu = int(input("> "))

    if (menu == 1):
        base(2)
    elif (menu == 2):
        url(2)
    elif (menu == 3):
        rsa(2)
    else:
        print("EXIT... BYEBYE")



printEmotion()
printCrypto()
printEndecode()


print("Select the number…")
print("1. ENCRYPT")
print("2. DECRYPT")
print("ANY OHTER NUMBER TO EXIT...")
menu = int(input("> "))

if (menu == 1):
    encode()
elif (menu == 2):
    decode()
else:
    print("EXIT... BYEBYE")

