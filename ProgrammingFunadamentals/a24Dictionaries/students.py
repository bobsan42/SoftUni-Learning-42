def students():
    command = ''
    data = {}
    while True:
        command = input()
        if ':' in command:
            x = command.split(':')
            data[x[1]] = {"name": x[0], "course": x[2]}
        else:
            break

    for (id, student) in data.items():
        if student["course"].lower() == command.replace('_',' ').lower():
            print(f"{student['name']} - {id}")


students()
