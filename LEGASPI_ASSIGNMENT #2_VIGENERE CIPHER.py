#LEGASPI, LANA CAZANDRA U. - BSCPE 1-5

moredata = "yes"
while moredata == "yes":

#introduction
    user = input("Enter username: ")
    print ("\nWelcome to the program " + user, "!\n")

    print ("PROGRAM #3: VIGENERE CIPHER".center(50,("-")))

#listing the letters
    letters_of_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    letter_to_cipher = dict(zip(letters_of_alphabet, range(len(letters_of_alphabet))))
    cipher_to_letter = dict(zip(range(len(letters_of_alphabet)), letters_of_alphabet))

#encrypting message
    def encrypt(message, key):
        encrypted = ""
        split_message = [
            message[i : i + len(key)] for i in range(0, len(message), len(key))
        ]

        for each_split in split_message:
            i = 0
            for letter in each_split:
                number = (letter_to_cipher[letter] + letter_to_cipher[key[i]]) % len(letters_of_alphabet)
                encrypted += cipher_to_letter[number]
                i += 1

        return encrypted

#decrypting message
    def decrypt(cipher, key):
        decrypted = ""
        split_encrypted = [
            cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
        ]

        for each_split in split_encrypted:
            i = 0
            for letter in each_split:
                number = (letter_to_cipher[letter] - letter_to_cipher[key[i]]) % len(letters_of_alphabet)
                decrypted += cipher_to_letter[number]
                i += 1

        return decrypted

#listing the key and message
    def main():
        message = "THISISTHELASTTASKHOORDAY"
        key = "KNIGHT"
        encrypted_mssg = encrypt(message, key)
        decrypted_mssg = decrypt(encrypted_mssg, key)

#final output
        print("\nOriginal message: " + message)
        print("Encrypted message: " + encrypted_mssg)
        print("Decrypted message: " + decrypted_mssg)


    main()

    print ("\nNOTE: If you wanted to run the program again, strictly answer 'yes' in lowercase. Failure to do so will end the program.\n")
    moredata = str(input("Would you like to run the program again?: "))
