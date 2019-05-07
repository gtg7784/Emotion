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
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

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

def base(cyptotype):
    print("base64 type is", end=" ")
    print(cyptotype)
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
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator) #generate pub and priv key

        publickey = key.publickey() # pub key export for exchange

        encrypted = publickey.encrypt('encrypt this message', 32)
        #message to encrypt is in the above line 'encrypt this message'

        print ('encrypted message:', encrypted) #ciphertext
        f = open ('encryption.txt', 'w')
        f.write(str(encrypted)) #write ciphertext to file
        f.close()

        

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

