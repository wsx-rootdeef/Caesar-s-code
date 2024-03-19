def decrypt_caesar_cipher(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        key += 1  # 计算每个字符的移动位数
        plaintext += chr((ord(ciphertext[i]) - ord('a') + key) + ord('a'))  # 解密每个字符
    return plaintext

# 测试代码
ciphertext = "afZ_r9VYfScOeO_UL^RWUc"
key = 4
decrypted_text = decrypt_caesar_cipher(ciphertext, key)
print("密文:", ciphertext)
print("解密后:", decrypted_text)