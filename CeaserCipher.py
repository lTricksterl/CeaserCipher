import argparse
import os
import sys

def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97 #65 is correspond to the ASCII values of the lowercase 'a' and 97 to uppercase 'A'
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(encrypted_message, shift):
    return caesar_cipher_encrypt(encrypted_message, -shift)
def main():
    parser = argparse.ArgumentParser(prog='CaesarCipher',description='Encrypt or decrypt text using the Caesar Cipher algorithm.')
    parser.add_argument('-e','--encrypt',action='store_true',help='Encrypt the text')
    parser.add_argument('-d','--decrypt',action='store_true',help='Decrypt the text')
    parser.add_argument('-f', '--file',type=str, help='Path to the input file')
    parser.add_argument('-s','--save',type=str,help='Path to save the output file')
    parser.add_argument('shift',type=int,help='Shift value for the Caesar Cipher')
    parser.add_argument('text',nargs='*',help='The text to encrypt or decrypt (ignored if -f is used)')
    args = parser.parse_args()
    if not (args.encrypt or args.decrypt):
        sys.exit("Error: Please use -e for encryption or -d for decryption.")

    if args.encrypt and args.decrypt:
        sys.exit("Error: You can only choose one  (encryption or decryption) but not at the same time.")
    
    if args.file:
        if not os.path.isfile(args.file):
            sys.exit(f"Error: File '{args.file}' not found.")
        with open(args.file, 'r') as file:
            text = file.read()
    else:
        if not args.text:
            sys.exit("Error: Please provide text to encrypt or decrypt.")
        text = " ".join(args.text)

    result = caesar_cipher_encrypt(text, args.shift) if args.encrypt else caesar_cipher_decrypt(text, args.shift)
    
    if args.save:
        with open(args.save, 'w') as output_file:
            output_file.write(result)
        print(f"Result saved to {args.save}")
    else:
        print(result)

if __name__ == "__main__":
    main()