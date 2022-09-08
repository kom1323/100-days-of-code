import pandas as pd



data = pd.read_csv(r".\day26-NATO_alphabet\nato_phonetic_alphabet.csv")

data_dic = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ")

lst = [data_dic[letter] for letter in word.upper()]
print(lst)