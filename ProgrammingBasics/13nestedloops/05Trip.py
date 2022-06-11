destination = input()
budget_min = 0.0

while destination != 'End':
    budget_min = float(input())
    saved = 0
    while saved < budget_min:
        x = float(input())
        saved += x
    if saved >= budget_min:
        print(f'Going to {destination}!')
    destination = input()
