exam_results = {}  # {username: {language: points}}
languages = {}  # {language: submissions_count}

while True:
    command = input()
    if command == 'exam finished':
        break
    info = command.split('-')
    username = info[0]
    if info[1] == 'banned':
        if username in exam_results.keys():
            exam_results.pop(username)
        continue

    lang = info[1]
    if lang not in languages.keys():
        languages[lang] = 0
    languages[lang] += 1

    score = int(info[2])

    if username not in exam_results.keys():
        exam_results[username] = {}
    if lang not in exam_results[username].keys():
        exam_results[username][lang] = 0
    if score > exam_results[username][lang]:
        exam_results[username][lang] = score

print("Results:")
for (user, results) in exam_results.items():
    for score in results.values():
        print(f"{user} | {score}")
print('Submissions:')
for (lang, submissions) in languages.items():
    print(f"{lang} - {submissions}")
