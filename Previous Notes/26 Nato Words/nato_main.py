import pandas

quote =  pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict ={row.letter:row.code for (index, row) in quote.iterrows()}

def generate_phonetic():
    word = input("enter a word: ").upper()
    try:
        nato_word = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry please use only letters")
        generate_phonetic()
    else:
        print(nato_word)

generate_phonetic()