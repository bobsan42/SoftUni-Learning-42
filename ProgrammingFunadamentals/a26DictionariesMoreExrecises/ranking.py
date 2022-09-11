dict_contest = {}  # {contest name: password}
dict_submission = {}  # {username:{contest:points}}


def check_if_valid(contest: str, password: str):
    if contest not in dict_contest.keys():
        return False
    if dict_contest[contest] != password:
        return False
    return True


def save_submission(username: str, contest: str, points: int):
    if username not in dict_submission.keys():
        dict_submission[username] = {}
    if contest not in dict_submission[username].keys():
        dict_submission[username][contest] = 0
    if points > dict_submission[username][contest]:
        dict_submission[username][contest] = points


def ranking():
    while True:
        input_line = input()
        if input_line == 'end of contests':
            break
        # print(input_line)
        contest = input_line.split(':')[0]
        password = input_line.split(':')[1]
        dict_contest[contest] = password

    while True:
        input_line = input()
        if input_line == 'end of submissions':
            break
        submission = input_line.split('=>')
        contest = submission[0]
        password = submission[1]
        username = submission[2]
        points = int(submission[3])
        if check_if_valid(contest, password):
            save_submission(username, contest, points)
    best_candidate = ''
    best_score = 0
    for (candidate, data) in dict_submission.items():
        if sum(data.values()) > best_score:
            best_score = sum(data.values())
            best_candidate = candidate

    print(f'Best candidate is {best_candidate} with total {best_score} points.')
    print('Ranking:')
    for name in sorted(dict_submission.keys()):
        print(name)

        # for (contest, points) in dict_submission[name].items():
        #     print(f"# {contest} -> {points}")

        sort_results = sorted(dict_submission[name].items(), key=lambda x: x[1], reverse=True)

        for i in sort_results:
            print(f'#  {i[0]} -> {i[1]}')

ranking()