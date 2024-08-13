# https:#github.com/semihkagan/PhpVisitorSaver
# Lütfe#yorum satırlarını silmeyin :/ ❤️
import base64
import os
from colorama import Fore, init

title = "Base64 Decoder - Github : semihkagan"
os.system("@title " + title)
init(autoreset=True)

encoder_title = '''
  ____                   __ _  _     ______                     _           
 |  _ \                 / /| || |   |  ____|                   | |          
 | |_) | __ _ ___  ___ / /_| || |_  | |__   _ __   ___ ___   __| | ___ _ __ 
 |  _ < / _` / __|/ _ \ '_ \__   _| |  __| | '_ \ / __/ _ \ / _` |/ _ \ '__|
 | |_) | (_| \__ \  __/ (_) | | |   | |____| | | | (_| (_) | (_| |  __/ |   
 |____/ \__,_|___/\___|\___/  |_|   |______|_| |_|\___\___/ \__,_|\___|_|   v1.0.0
                                                                            
'''
load_title = encoder_title + "Source Code: \033[4mhttps://github.com/semihkagan/PythonBase64Decompiler\033[0m\n"

example_inputfile = '''
// Example Input File
// This is a comment line 
aGVsbG8gd29ybGQ=
V2VsY29tZSB0byBteSBwcm9qZWN0

Q2hlY2sgb3V0IG15IHJlcG9zaXRvcnk=

RGV2ZWxvcGVkIGJ5IEdpdGhidWIhIHNlbWloa2FnYW4=
R2l0aHViOiBzZW1paGthZ2Fu
UGxlYXNlIGxpa2UgYW5kIHN0YXIgbXkgcmVwb3NpdG9yeQ==
'''

def decode_base64(encoded_str):
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        return decoded_bytes.decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error decoding string: {e}"
    
def read_and_decode_file(filename):
    decoded_strings = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('//'):  # Boş satırları ve başında // olan atla
                    decoded_strings.append(decode_base64(line))
    except FileNotFoundError:
        return [Fore.RED + "File not found."]
    except Exception as e:
        return [Fore.RED +  f"Error reading file: {e}"]
    
    return decoded_strings

def create_and_write_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

if __name__ == "__main__":
    create_and_write_to_file("input.txt",example_inputfile)
    while True:
     os.system("cls")
     print(load_title)
     print(Fore.LIGHTYELLOW_EX + "\nEnter Base64 Code or,\nEnter the name of the input file or path:")
     command = str(input(Fore.YELLOW + "> " + Fore.LIGHTWHITE_EX))

     print("\n---------------------------------------\n")
     if '.' in command:
        decoded_strings = read_and_decode_file(command)
        for i, s in enumerate(decoded_strings):
            print(Fore.LIGHTBLUE_EX + "Decoded string" + Fore.BLUE + f" [{i}]: " + Fore.LIGHTWHITE_EX + f"{s}")
        total_texts = len(decoded_strings)
     else:
        print(Fore.LIGHTBLUE_EX + "Decoded string" + Fore.BLUE + f" [0]: " + Fore.LIGHTWHITE_EX + decode_base64(command))
        total_texts = 1
     print("\n---------------------------------------\n")

     print(Fore.LIGHTGREEN_EX + f"Decoding Syuccessfuly! , total decompiled texts({total_texts}) .")
     input("\nPlease press enter to continue...")

# https://github.com/semihkagan tarafından yazılmıştır.
