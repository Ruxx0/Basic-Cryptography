from cryptography.fernet import Fernet
import sys

def decrypt_file(input_file, output_file, key_file):
    with open(key_file, 'rb') as f:
        key = f.read()

    fernet = Fernet(key)

    # Read ciphertext
    with open(input_file, 'rb') as f:
        ciphertext = f.read()

    # Decrypt data
    plaintext = fernet.decrypt(ciphertext)

    # Write plaintext to output file
    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"File decrypted and saved to {output_file}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python decryptfile.py <input_file> <output_file> <key_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    key_file = sys.argv[3]

    decrypt_file(input_file, output_file, key_file)

if __name__ == '__main__':
    main()

