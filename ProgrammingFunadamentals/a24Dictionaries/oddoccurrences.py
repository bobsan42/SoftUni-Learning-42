def odd_occurrences():
    some_words = input().split(' ')
    occurrences = {}
    for word in some_words:
        word = word.lower()
        if not word in occurrences.keys():
            occurrences[word] = 0
        occurrences[word] += 1
    for (word, count) in occurrences.items():
        if count % 2 == 1:
            print(word, end=' ')

odd_occurrences()