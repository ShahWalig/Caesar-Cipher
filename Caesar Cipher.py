alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encryption(plain_text, shift_key, operation):
    cipher_text = ''

    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            if operation == 'd':
                new_position = (position - shift_key) % 26
            else:
                new_position = (position + shift_key) % 26

            cipher_text += alphabet[new_position]
        else:
            cipher_text += char

    print(f"After Action here is text: {cipher_text}")


# Uncomment the following function if you want to include decryption functionality
# def decryption(cipher_text, shift_key):
#     decrypted_text = ''
#     for char in cipher_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = (position - shift_key) % 26
#             decrypted_text += alphabet[new_position]
#         else:
#             decrypted_text += char
#     print(f"Decrypted text: {decrypted_text}")

star = True

# while star:
#     action = input("Encryption or Decryption (e/d): ").lower()
#     if action != 'e' and action != 'd':
#         print("Invalid option. Please enter 'e' for encryption or 'd' for decryption.")
#     else:
#         user_text = input("Enter your text for action: ").lower()
#         user_shift_key = int(input("Enter your shift key (number): "))
#
#         if action == 'd':
#             encryption(user_text, user_shift_key, 'd')
#         elif action == 'e':
#             encryption(user_text, user_shift_key, 'e')
#
#         star = input("To stop, press 'n'. To continue, press 'c': ").lower()
#         if star == 'n':
#             star = False




while star:
    action = input("Encryption or Decryption (e/d): ").lower()
    if action != 'e' and action != 'd':
        print("Invalid option. Please enter 'e' for encryption or 'd' for decryption.")

    else:
        user_text = input("Enter your text for Action: ").lower()
        user_shift_key = int(input("Enter your shift key (number): "))

        if action == 'd':
            encryption(user_text, user_shift_key, 'd')
        elif action == 'e':
            encryption(user_text, user_shift_key, 'e')
        else:
            print("Invalid option. Please enter 'e' for encryption or 'd' for decryption.")

        star = input("To stop, press 'n'. To continue, press 'c': ").lower()
        if star == 'n':
            star = False
