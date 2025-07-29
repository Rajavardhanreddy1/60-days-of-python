
# Problem: Compress a String (Run-Length Encoding)
# 📝 Description:
# Write a Python program that compresses a string using the following run-length encoding technique:
# Consecutive characters are replaced with the character followed by the count of its repetition.
# 📥 Input:

# s = "aaabbccccdaa"
# 📤 Output:

# a3b2c4d1a2
# ✅ Rules:
# The compression is case-sensitive (A and a are different).

# If a character appears only once, still include it with 1.

# Only letters are given (no spaces, digits, or symbols).def compress_string(s):
def compress_string(s):
    if not s:
        return ""

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result

input_str = "aaabbccccdaa"
compressed = compress_string(input_str)
print("Compressed string:", compressed)
