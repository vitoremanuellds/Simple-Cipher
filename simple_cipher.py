def simple_cipher(text):
    
    def get_alphabet_number(letter):
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        if letter.islower() or letter.isnumeric():
            return (alphabet.find(letter), False)
        return (alphabet.find(letter.lower()), True)

    def generate_new_letter(alphabet_number, previous_shift, is_upper):
        shift = (previous_shift + alphabet_number)
        new_letter_index = (shift) % 36
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

        if is_upper:
            if alphabet[new_letter_index].isnumeric():
                return (alphabet[new_letter_index], shift)
            return (alphabet[new_letter_index].upper(), shift)
        return (alphabet[new_letter_index], shift)
    
    previous_shift = get_alphabet_number(text[0])[0]
    
    new_text = ""

    for i in range(len(text)):
        alphabet_number = get_alphabet_number(text[i])
        new_letter = generate_new_letter(alphabet_number[0], previous_shift, alphabet_number[1])
        new_text += new_letter[0]
        previous_shift = new_letter[1]

    return new_text

text = input("Digite o texto que quer converter: ")
print("Texto convertido:", simple_cipher(text))
    
