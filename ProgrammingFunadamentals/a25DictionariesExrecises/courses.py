courses = {}

while True:
    command = input()
    if command == 'end':
        break
    data = command.split(' : ')
    course_name = data[0]
    student_name = data[1]
    if course_name not in courses.keys():
        courses[course_name]=[]
    courses[course_name].append(student_name)

for course in courses.keys():
    print(f'{course}: {len(courses[course])}')
    for student in courses[course]:
        print(f'-- {student}')
