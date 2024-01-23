# Day 26 - Project:  NATO Alphabet #

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo}

nato_alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
another_word = True
while another_word:
    word = input("Enter a word:  ").upper()
    nato_words = [nato_alphabet_dict[letter] for letter in word]
    print(nato_words)

    if input("Enter another word? 'Y' or 'N'  ").lower() == 'n':
        break
