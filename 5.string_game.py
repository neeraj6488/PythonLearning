word = input("Enter a word: ")

word_length = len(word)

print(f"The word '{word}' has {word_length} characters")

# Reverse the word
word_reverse = word[::-1]

print(f"The reversed word is '{word_reverse}'")

# Creae new word
first_char = word[0]
new_word = first_char * word_length

print(f"The new word is '{new_word}'")

# Concat the word
suffix = 'ish'
suffix_word = word + suffix

print(f"The suffix word is '{suffix_word}'")

# Upper case
print(f"The upper case word is '{word.upper()}'")

# Replace
print(f"Replacing 'n' word is '{word.replace('n','x')}'")
