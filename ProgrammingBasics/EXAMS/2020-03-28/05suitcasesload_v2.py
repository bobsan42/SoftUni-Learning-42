x = input()
capacity = float(x)

free_space = capacity
n_suitcases = 0
is_finished = False
is_full = False

while True:
    x = input()
    if x == 'End':
        is_finished = True
        break
    y = float(x)
    if (n_suitcases + 1) % 3 == 0:
        y *= 1.1
    if free_space < y:
        is_full = True
        break
    free_space -= y
    n_suitcases += 1
    if free_space == 0:
        is_finished = True
        break

if is_finished:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")

print(f"Statistic: {n_suitcases} suitcases loaded.")
