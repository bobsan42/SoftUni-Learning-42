n_students = int(input())
grades_stats_list = [0, 0, 0, 0]
total_grades = 0

for i in range(n_students):
    grade = float(input())
    total_grades += grade

    if grade < 3:
        grades_stats_list[0] += 1
    elif grade < 4:
        grades_stats_list[1] += 1
    elif grade < 5:
        grades_stats_list[2] += 1
    elif grade >= 5:
        grades_stats_list[3] += 1

print(f"Top students: {(grades_stats_list[3] / n_students * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(grades_stats_list[2] / n_students * 100):.2f}%")
print(f"Between 3.00 and 3.99: {(grades_stats_list[1] / n_students * 100):.2f}%")
print(f"Fail: {(grades_stats_list[0] / n_students * 100):.2f}%")
print(f"Average: {(total_grades / n_students):.2f}")
