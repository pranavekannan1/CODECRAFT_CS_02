## ENCDEC_CIPHER

This is a simple Python program that encrypts and decrypts messages using the Caesar Cipher technique.

##  What is Caesar Cipher?

Caesar Cipher is one of the oldest and simplest encryption methods. Each letter in the message is shifted by a fixed number of positions in the alphabet.

For example, with a shift of 3:
- A becomes D
- B becomes E
- X becomes A (wraps around)

##  Features

- Encrypt any text message using a shift number
- Decrypt an encrypted message using the same shift
- Works with both uppercase and lowercase letters
- Leaves numbers, symbols, and spaces unchanged

##  How to Use

1. Run the Python file (eg `caesar_cipher.py`)
2. Choose:
   - `E` for encryption
   - `D` for decryption
3. Enter your message
4. Enter the shift number (e.g., 3)
5. See the encrypted or decrypted result

## Example

Do you want to (E)ncrypt or (D)ecrypt? E
Enter your message: PRANAVE KANNAN
Enter the shift value : 3
Encrypted Message: SUDQDYH NDQQDQ

Do you want to (E)ncrypt or (D)ecrypt? D
Enter your message: SUDQDYH NDQQDQ
Enter the shift value : 3
Decrypted Message: PRANAVE KANNAN

## How it Works

+ Uses ASCII values to shift each character
+ Wraps letters around using `% 26` to stay within A-Z or a-z range
+ Ignores special characters or digits

## Requirements

+ Python 
+ No external libraries needed

