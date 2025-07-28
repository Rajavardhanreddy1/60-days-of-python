 # problem: Count Vowels and Consonants
# 📝 Description:
# Write a Python program that takes a string from the user and counts how many vowels and consonants are in it.
# 📥 Input Example:
# Enter a string: Hello World
# 📤 Expected Output:
# Vowels: 3  
# Consonants: 7
# ✅ Rules:
# Ignore spaces, digits, and special characters.

# Count only alphabetic letters.

# Consider vowels as: a, e, i, o, u (both uppercase and lowercase).

# All other alphabetic characters are consonants.
def count_vow_con(text):
    a="aeiouAEIOU"
    vow=0
    con=0
    for i in text:
        if i.isalpha():
            if i in a:
                vow+=1
            else:
                con+=1
        else:
            pass
    return vow,con
a,b=count_vow_con('Hello World')
print("vowels = ",a)
print("constants = ",b)
