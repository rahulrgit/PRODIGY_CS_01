def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# User Input
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

encrypted = encrypt(message, shift_value)
decrypted = decrypt(encrypted, shift_value)

print("\nEncrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
