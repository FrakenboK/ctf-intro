def rot(text, shift):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

ciphertext = "xdsy{Mk3_Y00v_Uqhzwj$!}"

print("Перебор всех сдвигов ROT:")
print("-" * 40)

for shift in range(26):
    decrypted = rot(ciphertext, shift)
    print(f"ROT{shift:2d}: {decrypted}")