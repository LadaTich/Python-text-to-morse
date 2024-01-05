letters_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

user_input = input("\nWrite a text to convert:\n\n")

def convert():
    morse_list = []
    [morse_list.append(morse_alphabet[letters_alphabet.index(letter)]) for letter in user_input]

    print(morse_list)

convert()