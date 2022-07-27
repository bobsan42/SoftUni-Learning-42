companies = {}

while True:
    command = input()
    if command == "End":
        break
    info = command.split(' -> ')
    if info[0] not in companies.keys():
        companies[info[0]] = []
    if info[1] not in companies[info[0]]:
        companies[info[0]].append(info[1])

for company in companies.keys():
    print(company)
    for user in companies[company]:
        print(f'-- {user}')
