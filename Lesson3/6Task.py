def int_func(eng_word):
    new_word = ''
    for l in eng_word:
        if not 97 <= ord(l) <= 122:
            print(f'{l} - не маленькая латинская буква ')
        else:
            new_word += (l if new_word != '' else chr(ord(l)-32))
    return new_word

my_word = input("Введитн cлово из маленьких латинских букв: ")
print(f'{my_word} - {int_func(my_word)}')

my_words = input("Введите несколько cлов из маленьких латинских букв: ").split()
for w in range(len(my_words)):
    my_words[w] = int_func(my_words[w])
for w in my_words:
    print(w, end=' ')