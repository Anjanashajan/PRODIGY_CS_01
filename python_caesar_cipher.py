letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters= len(letters)

def encrypt(plaintext,key):
    ciphertext=''
    for letter in plaintext:
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext +=letter
            else:
                    new_index =index + key
                    if new_index >= num_letters:
                        new_index-=num_letters
                    ciphertext += letters[new_index]
    return ciphertext

def encrypt(ciphertext,key):
    plaintext=''
    for letter in ciphertext:
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext +=letter
            else:
                    new_index =index + key
                    if new_index < 0:
                        new_index+=num_letters
                    plaintext += letters[new_index]
    return plaintext


print()
print('*** caesar cipher program')
print()

print('Do you want to encrypt or decrypt?')
user_input =input('e/d:').lower()
print()

if user_input == 'e':
    print('encryption mode selected')
    print()
    key =int(input('entert the key( 1 through 26):'))
    text = input('enter the text to encrypt: ')
    ciphertext = encrypt(text,key)
    print(f'ciphertext:{ciphertext}')
elif user_input == 'd':
    print('decryption mode selected')
    print()
    key =int(input('entert the key( 1 through 26):'))
    text = input('enter the text to decrypt: ')
    plaintext = encrypt(text,key)
    print(f'plaintext:{plaintext}')


