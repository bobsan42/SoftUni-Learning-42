n_juri = int(input())
presentation_name = input()
grades_count = 0
grades_sum = 0

while presentation_name != 'Finish':
    p_grades_sum = 0
    for i in range(n_juri):
        x = float(input())
        p_grades_sum += x
        grades_sum += x
        grades_count += 1
    print(f'{presentation_name} - {(p_grades_sum / n_juri):.2f}.')
    presentation_name = input()

print(f'Student\'s final assessment is {(grades_sum / grades_count):.2f}.')
