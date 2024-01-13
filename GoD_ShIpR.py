from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
from colorama import Fore, Style, init

# Install colorama if not already installed
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama

colorama.init(autoreset=True)

def print_shipr_logo():
    # The SHIPR logo goes here
    shipr_logo = [
        "   ____            _     _      _____",
        "  / __ \\          (_)   | |    / ____|",
        " | |  | |_ __ __ _ _ ___| |__ | |  __  __ _ _ __ ___   __ _",
        " | |  | | '__/ _` | / __| '_ \\| | |_ |/ _` | '_ ` _ \\ / _` |",
        " | |__| | | | (_| | \\__ \\ | | | |__| | (_| | | | | | | (_| |",
        "  \\____/|_|  \\__, |_|___/_| |_|\\_____|\\__, |_| |_| |_|\\__,_|",
        "   SHIPR       __/ |                       __/ |",
        "              |___/                       |___/",
    ]

    colors = [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.RED, Fore.BLUE, Fore.WHITE]

    for i, line in enumerate(shipr_logo):
        color = colors[i % len(colors)]
        print(color + line + Style.RESET_ALL)
    print()

def generate_aes_key():
    return os.urandom(32)  # 256 bits for AES-256

def generate_des_key():
    return os.urandom(16) * 2  # 128 bits for Triple DES (two blocks of 64 bits each)

def generate_iv(algorithm):
    return os.urandom(algorithm.block_size // 8)

def encrypt(message, key, iv, algorithm):
    try:
        padder = padding.PKCS7(algorithm.block_size).padder()
        padded_data = padder.update(message.encode()) + padder.finalize()

        cipher = Cipher(algorithm(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return ciphertext, algorithm.name
    except Exception as e:
        print(f"Encryption error: {e}")
        return None, None

def decrypt_message(ciphertext, keys, algorithms):
    for key, algorithm in zip(keys, algorithms):
        try:
            iv = ciphertext[:algorithm.block_size // 8]
            ciphertext = ciphertext[algorithm.block_size // 8:]

            if len(ciphertext) % algorithm.block_size != 0:
                raise ValueError("Ciphertext length is not a multiple of the block size.")

            cipher = Cipher(algorithm(key), modes.CFB(iv), backend=default_backend())
            decryptor = cipher.decryptor()

            data = decryptor.update(ciphertext) + decryptor.finalize()
            ciphertext = data
        except Exception as e:
            print(f"Decryption error with algorithm {algorithm}: {e}")
            return None

    return ciphertext.decode() if ciphertext is not None else None

def display_encryption_methods():
    print(Fore.BLUE + "\nAvailable Encryption Methods:" + Style.RESET_ALL)
    print(Fore.BLUE + "1. AES (Advanced Encryption Standard)")
    print("2. Triple DES (Data Encryption Standard)" + Style.RESET_ALL)

def display_help():
    print(Fore.BLUE + "\nAvailable Actions:" + Style.RESET_ALL)
    print(Fore.BLUE + "1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Retrieve original unencrypted word")
    print("4. Clear the terminal")
    print("5. Exit the program")
    print("6. Help (display this menu)" + Style.RESET_ALL)

def get_valid_input(prompt, options):
    while True:
        print(Fore.YELLOW + prompt + Style.RESET_ALL, end="")
        user_input = input()

        if user_input.lower() == 'exit':
            return 'exit'
        if user_input.lower() == 'help':
            return 'help'
        if user_input.lower() == 'clear':
            os.system('clear' if os.name == 'posix' else 'cls')
            continue
        if user_input.isdigit() and 1 <= int(user_input) <= options:
            return int(user_input)
        print(Fore.RED + "Invalid input. Please enter a valid number or type 'exit' to exit." + Style.RESET_ALL)

keys = []
original_word = ""
while True:
    print_shipr_logo()
    user_input = get_valid_input("Enter a command ('exit' to exit, 'help' for available actions): ", 7)

    if user_input == 'exit':
        print(Fore.RED + "Exiting the program." + Style.RESET_ALL)
        break

    elif user_input == 'help':
        display_help()

    elif user_input == 1:
        message = input("Enter the message you want to encrypt: ")
        display_encryption_methods()
        encryption_choice = get_valid_input("Choose Encryption Method (1-2): ", 2)
        encryption_methods = [
            (generate_aes_key, algorithms.AES),
            (generate_des_key, algorithms.TripleDES),
        ]
        keys = [key_gen() for key_gen, _ in encryption_methods]

        method_name = None
        for i in range(encryption_choice):
            _, algorithm = encryption_methods[i]
            key = keys[i]
            iv = generate_iv(algorithm)

            ciphertext, method_name = encrypt(message, key, iv, algorithm)
            if ciphertext is None:
                print(Fore.RED + "Encryption failed." + Style.RESET_ALL)
                break

        print(Fore.GREEN + f"\nFinal Encrypted Message (using {method_name}): {ciphertext}" + Style.RESET_ALL)

    elif user_input == 2:
        if not keys:
            print(Fore.RED + "No keys available. Please encrypt a message first." + Style.RESET_ALL)
            continue

        encrypted_message = input("Enter the message you want to decrypt: ")
        decrypted_message = decrypt_message(encrypted_message.encode(), keys, [algo for _, algo in encryption_methods])

        if decrypted_message is not None:
            print(Fore.GREEN + "Decrypted Message:", decrypted_message + Style.RESET_ALL)
        else:
            print(Fore.RED + "Decryption failed. Please try a different message." + Style.RESET_ALL)

    elif user_input == 3:
        print(Fore.BLUE + f"Original Unencrypted Word: {original_word}" + Style.RESET_ALL)

    elif user_input == 4:
        os.system('clear' if os.name == 'posix' else 'cls')

    elif user_input == 5:
        print(Fore.RED + "Exiting the program." + Style.RESET_ALL)
        break

    elif user_input == 6:
        display_help()

    elif user_input == 7:
        original_word = input("Enter the original unencrypted word: ")
        print(Fore.BLUE + f"Original unencrypted word set to: {original_word}" + Style.RESET_ALL)

