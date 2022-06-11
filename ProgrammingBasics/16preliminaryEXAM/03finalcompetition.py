n_dancers = int(input())
n_scores = float(input())
season = input()
location = input()
expenses_percent = 0
reward = n_dancers * n_scores

if location == 'Bulgaria':
    if season == 'summer':
        expenses_percent = 5
    elif season == 'winter':
        expenses_percent = 8
elif location == 'Abroad':
    reward *= 1.5
    if season == 'summer':
        expenses_percent = 10
    elif season == 'winter':
        expenses_percent = 15
reward *= (100 - expenses_percent) / 100

charity = .75 * reward
personal_reward = (.25 * reward) / n_dancers
print(f'Charity - {charity:.2f}')
print(f'Money per dancer - {personal_reward:.2f}')
