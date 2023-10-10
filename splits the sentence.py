# Requesting a sentence from the user
sentence = input("Please enter a sentence: ")

# Convert the sentence to uppercase
upper_sentence = sentence.upper()

# Split the sentence into a list of words
word_list = upper_sentence.split()

# Print the total number of words in the sentence
print(f"There are {len(word_list)} words in your sentence")

# For each word in the list, print the word, its length, and the count of 'B's it contains
for word in word_list:
    letter_count = len(word)
    b_count = word.count('B')
    print(f"{word} has {letter_count} letters and {b_count} 'B's")
