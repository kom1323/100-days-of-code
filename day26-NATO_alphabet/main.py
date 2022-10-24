import pandas as pd



data = pd.read_csv(r".\day26-NATO_alphabet\nato_phonetic_alphabet.csv")

data_dic = {row.letter:row.code for (index, row) in data.iterrows()}


while True:
    word = input("Enter a word: ").upper()
    try:
        lst = [data_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break
print(lst)