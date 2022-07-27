def avg(num_list):
    return sum(num_list) / len(num_list)


n = int(input())
data = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in data.keys():
        data[name] = {'avg': 0, 'grades': []}
    data[name]['grades'].append(grade)
    data[name]['avg'] = avg(data[name]['grades'])

to_remove = []
for (name, info) in data.items():
    if info['avg'] < 4.50:
        to_remove.append(name)
for name in to_remove:
    data.pop(name)
for (name, info) in data.items():
    print(f"{name} -> {info['avg']:.2f}")
