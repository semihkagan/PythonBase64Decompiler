# https:#github.com/semihkagan/PhpVisitorSaver
# Lütfe#yorum satırlarını silmeyin :/ ❤️
import base64
from colorama import Fore

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
        return [Fore.RED + "File not found." + Fore.RESET]
    except Exception as e:
        return [Fore.RED +  f"Error reading file: {e}" + Fore.RESET]
    
    return decoded_strings

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "Enter the name of the input file or path:")
    filename = str(input(Fore.YELLOW + "> " + Fore.LIGHTWHITE_EX))
    if(filename == "" or filename == " "):
        filename = "input.txt"
    decoded_strings = read_and_decode_file(filename)

    print("\n---------------------------------------\n")
    for i, s in enumerate(decoded_strings):
        print(Fore.LIGHTBLUE_EX + "Decoded string" + Fore.BLUE + f" [{i}]: " + Fore.LIGHTWHITE_EX + f"{s}" + Fore.RESET)
    print("\n---------------------------------------\n")

    total_file = len(decoded_strings)
    print(Fore.LIGHTGREEN_EX + f"Decoding Syuccessfuly! , total decompiled texts({total_file}) ." + Fore.RESET)
# https://github.com/semihkagan tarafından yazılmıştır.

