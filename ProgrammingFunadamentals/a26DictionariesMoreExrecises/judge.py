dict_results = {}  # {contest:{username:points}}
dict_contests = {}
dict_submissions = {}


def save_submission(username: str, contest: str, points: int):
    if username not in dict_results.keys():
        dict_results[username] = {}
    if contest not in dict_results[username].keys():
        dict_results[username][contest] = 0

    if contest not in dict_contests.keys():
        dict_contests[contest] = {}
    if username not in dict_contests[contest].keys():
        dict_contests[contest][username] = 0

    if points > dict_results[username][contest]:
        dict_results[username][contest] = points
        dict_contests[contest][username] = points

    i = len(dict_submissions) + 1
    dict_submissions[i] = {'user': username, 'contest': contest, 'score': points}


def judge():
    while True:
        input_line = input()
        if input_line == 'no more time':
            break
        submission = input_line.split(' -> ')
        username = submission[0]
        contest = submission[1]
        points = int(submission[2])
        save_submission(username, contest, points)

    for contest in dict_contests:
        print(f'{contest}: {len(dict_contests[contest])} participants')
        results = sorted(dict_contests[contest].items(), key=lambda x: x[1], reverse=True)
        j = 0
        for i in results:
            j += 1
            print(f'{j}. {i[0]} <::> {i[1]}')

    print('Individual standings:')
    total_scores = {}
    for x in dict_results.items():
        # print(x[0],x[1])
        total_scores[x[0]]=sum(x[1].values())
    # total_scores = {x[0]: sum(x[1].values()) for x in dict_results}
    sort_results = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)
    j = 0
    for i in sort_results:
        j += 1
        print(f'{j}. {i[0]} -> {i[1]}')


judge() #TODO - softuni judge 66/100
