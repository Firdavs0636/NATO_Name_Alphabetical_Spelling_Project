import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

encrypted = []


def generate_phonetic():
    user_name = input('Enter Your Name: ').upper()
    try:
        output_list = [phonetic_dictionary[letter] for letter in user_name]
    except KeyError:
        print('Only ALPHABETICAL characters please!')
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()


# Below code is another approach for this problem which uses dictionary key:value as a letter:code combination
# for letter in user_name:
#     name_letters = {letter: code for (key, code) in phonetic_dictionary.items() if letter == key}
#     encrypted.append(name_letters)

