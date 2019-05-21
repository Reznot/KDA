def encode(text_to_encode):
    text = text_to_encode.replace(" ", "")
    print(f"\nUsunięto spacje: {text}")
    print("Tworze pusty słownik\n")
    dicionary = {}
    tmp = ''
    dict_index = 0
    last_word_index = 0
    code = []

    for index in range(len(text)):
        tmp = tmp + text[index]
        if tmp not in dicionary:
            if tmp[:-1] == '':
                last_word_index = 0
            print(f"\nCiąg \"{tmp[:-1]}\" znajduje się w słowniku pod indexem {last_word_index}, dodaje do niego litere \"{tmp[-1]}\"")
            code.append(f"({last_word_index}, k({tmp[-1]}))")
            dict_index += 1
            print(f"Dodaje do słownika: \"{tmp}\"")
            dicionary[tmp] = dict_index

            print("Obecnie słownik zawiera: ", end='')
            for k, v in  dicionary.items():
                print(f"{v}:{k}", end="  ")
            print("\nObecny kod: ")
            for k, v in enumerate(code):
                print(f"{k+1}: {v}")
            print("\n")
            tmp = ''
        else:
            last_word_index = dicionary[tmp]
        # input("Aby przejść dalej nacisnij enter\n")
    print("Zakodowano cały tekst!!!")
    return code

def decode(encoded):
    dicionary = {}



text_to_encode = input("Podaj tekst który chcesz zakodować: ")
encoded_text = encode(text_to_encode)

# input("Aby rozpocząć dekodowanie wciśnij enter")
decode(encoded_text)

# a-bar-array-by-barrayar-bay
