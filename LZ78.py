def encode(text_to_encode):
    text = text_to_encode.replace(" ", "")
    print("Rozpoczynam kodowanie LZ78")
    print(f"\nUsunięto spacje: {text}")
    print("Tworze pusty słownik\n")
    dicionary = {}
    tmp = ''
    dict_index = 0
    last_word_index = 0
    code = []
    encoded = []
    added_new = False

    for index in range(len(text)):
        tmp = tmp + text[index]
        if tmp not in dicionary:
            if tmp[:-1] == '':
                last_word_index = 0
            print(f"\nCiąg \"{tmp[:-1]}\" znajduje się w słowniku pod indexem {last_word_index}, dodaje do niego litere \"{tmp[-1]}\"")
            code.append(f"({last_word_index}, k({tmp[-1]}))")
            encoded.append(f"{last_word_index}:>{tmp[-1]}")
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
            added_new = True
        else:
            last_word_index = dicionary[tmp]
        if added_new:
            input("Aby kontynuować kodowanie wciśnij enter\n")
            added_new = False
    print("Zakodowano cały tekst!!!\n")
    return encoded

def decode(encoded):
    dicionary = {}
    dict_index = 1
    tmp = ""
    decoded_text = ""
    print("Rozpoczynam dekodowanie LZ78")

    for code in encoded:
        print(f"Kod: {code}")
        splitted = code.split(":>")
        splitted[0] = int(splitted[0])
        if splitted[0] == 0:
            print(f"Litera {splitted[1]} występuje po raz pierwszy i trafia do słownika\nZostaje dodana do zdekodowanego tekstu")
            dicionary[dict_index] = splitted[1]
            dict_index += 1
            decoded_text = decoded_text + splitted[1]
            print(f"Zdekodowany tekst: {decoded_text}\n")
        else:
            print(f"Pod indeksem {splitted[0]} w slowniku znajduje się \"{dicionary[splitted[0]]}\"")
            print(f"Dodaje literkę \"{splitted[1]}\"")
            tmp = dicionary[splitted[0]] + splitted[1]
            print(f"Dodaje do słownika \"{tmp}\"")
            dicionary[dict_index] = tmp
            dict_index += 1
            decoded_text = decoded_text + tmp
            print(f"Zdekodowany tekst: {decoded_text}\n")
        input("Aby kontynuować dekodowanie wcisnij enter\n")
    print("Tekst został odkodowany")

text_to_encode = input("Podaj tekst który chcesz zakodować: ")
encoded_text = encode(text_to_encode)
print("=======================================================\n")
input("Aby rozpocząć dekodowanie wciśnij enter\n")
decode(encoded_text)

# a-bar-array-by-barrayar-bay
