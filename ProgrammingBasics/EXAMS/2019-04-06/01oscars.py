x = input()
hall_rent = int(x)
statues = .7 * hall_rent
catering = .85 * statues
sound = .5 * catering
cost = hall_rent + statues + catering + sound
print(f'{cost:.2f}')
