
# Convert entire string to list of characters
def message_to_characters(string):
    return [char for char in string]

# Get key from dict using value
def get_key(val, alp_dict):
    for key, value in alp_dict.items():
         if val == value:
             return key

    return f"No such key found for {val}"

# Encrypt given message using caesar encryption
def caesar_encryption(message):

    alphabet_dict = {0: " ", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e",
        6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l",
        13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s",
        20: "t", 21: "u", 22: "v", 23: "x", 24: "y", 25: "z", 26: "ä", 27: "ö"}

    char_list = message_to_characters(message)
    encryption = ""
    """ Create encrypted char list with numeric values """
    for char in char_list:
        key = get_key(char, alphabet_dict)
        #print("Initial character in message ", key)
        key += 4
        key = key % (len(alphabet_dict) - 1)
        #print("Encrypted character in message ", key)
        encryption += alphabet_dict[key]

    return encryption

# Decrypt given message using caesar encryption
def caesar_decryption(message):

    alphabet_dict = {0: " ", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e",
        6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l",
        13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s",
        20: "t", 21: "u", 22: "v", 23: "x", 24: "y", 25: "z", 26: "ä", 27: "ö"}

    char_list = message_to_characters(message)
    decryption = ""

    """ Create decrypted char list with numeric values """
    for char in char_list:
        key = get_key(char, alphabet_dict)
        #print("Initial character in message ", key)
        key -= 4
        key = key % (len(alphabet_dict) - 1)
        #print("Decrypted character in message ", key)
        decryption += alphabet_dict[key]
        #print(encryption)

    return decryption


def main():
    crypted_message = caesar_encryption(input("give message to encrypt:"))
    print(f"\n\n encrypted message is: '{crypted_message}'")

    decrypted_message = caesar_decryption(input("give message to decrypt:"))
    print(f"\n decrypted message is: '{decrypted_message}'")

if __name__=="__main__":
    main()
