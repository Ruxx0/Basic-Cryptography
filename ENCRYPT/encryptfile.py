from cryptography.fernet import Fernet
import sys

def encrypt_file(input_file, output_file, key_file):
    with open(key_file, 'rb') as f:
        key = f.read()

    fernet = Fernet(key)

    # Read plaintext
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Encrypt data
    ciphertext = fernet.encrypt(plaintext)

    # Write ciphertext to output file
    with open(output_file, 'wb') as f:
        f.write(ciphertext)

    print(f"File encrypted and saved to {output_file}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python encryptfile.py <input_file> <output_file> <key_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    key_file = sys.argv[3]

    encrypt_file(input_file, output_file, key_file)

if __name__ == '__main__':
    main()

