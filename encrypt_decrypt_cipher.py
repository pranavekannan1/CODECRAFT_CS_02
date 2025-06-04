def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def caesar_cipher():
    print("<-----ENCDEC CIPHER----->")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose E or D.")
        return

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value : "))

    if choice == 'E':
        encrypted = encrypt(message, shift)
        print("Encrypted Message:", encrypted)
    else:
        decrypted = decrypt(message, shift)
        print("Decrypted Message:", decrypted)
caesar_cipher()