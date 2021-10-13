# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

vowel = "aeiou"
consonant = "bcdfghjklmnpqrstvwxyz"

ch = input("Please enter a letter from the alphabet (a-z or A-Z): ")

def e_one(c):

    if c.lower() in vowel:
        print(f"The letter {c} is a vowel")
    elif c.lower() in consonant:
        print(f"The letter {c} is a consonant")

e_one(ch) 

