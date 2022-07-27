def word_synonyms():
    words = {}
    words_count = int(input())

    for _ in range(words_count):
        word = input()
        if not word in words.keys():
            words[word] = []
        synonym = input()
        words[word].append(synonym)

    for (word,synonyms) in words.items():
        print(word, end=" - ")
        print(', '.join(synonyms))

word_synonyms()
