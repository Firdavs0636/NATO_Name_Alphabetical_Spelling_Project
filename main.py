import pandas as pd

# TODO 1. Create a dictionary in this format:
df = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

encrypted = []
user_name = input('Enter Your Name: ').upper()
output_list = [phonetic_dictionary[letter] for letter in user_name]
print(output_list)



# Below code is another approach for this problem which uses dictionary key:value as a letter:code combination
# for letter in user_name:
#     name_letters = {letter: code for (key, code) in phonetic_dictionary.items() if letter == key}
#     encrypted.append(name_letters)

