stop_phrase = "End of words"
vowels_list = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

most_powerful_word = ''
most_powerful_value = 0

a_word = input()
while a_word != stop_phrase:
    word_power = 0
    word_length = len(a_word)
    for letter in a_word:
        word_power += ord(letter)
    if a_word[0] in vowels_list:
        word_power *= word_length
    else:
        word_power = int(word_power / word_length)

    if word_power > most_powerful_value:
        most_powerful_word = a_word
        most_powerful_value = word_power

    a_word = input()

print(f'The most powerful word is {most_powerful_word} - {most_powerful_value}')
