# https://judge.softuni.org/Contests/Practice/Index/2305#0

def counter_strike():
    battles_won = 0
    init_energy = int(input())
    command = input()
    energy = init_energy
    is_failed = False
    while command != 'End of battle':
        distance = int(command)
        if energy < distance:
            print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
            is_failed = True
            break
        else:
            energy -= distance
            battles_won += 1
            if battles_won % 3 == 0:
                energy += battles_won
        command = input()

    if not is_failed:
        print(f"Won battles: {battles_won}. Energy left: {energy}")


# Driver code
if __name__ == '__main__':
    # function call
    counter_strike()
