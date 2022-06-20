# https://judge.softuni.org/Contests/Practice/Index/2517#1

def the_lift():
    max_people_in_wagon = 4
    people_waiting = int(input())
    init_lift_state = input()
    lift_state = list(map(int, init_lift_state.split()))
    no_more_people_in_queue = False
    lift_is_full = False
    while True:
        if people_waiting == 0:
            no_more_people_in_queue = True
            break
        if sum(lift_state) == len(lift_state) * max_people_in_wagon:
            lift_is_full = True
            break
        for idx, wagon in enumerate(lift_state):
            seats_free = max_people_in_wagon - wagon
            if people_waiting >= seats_free:
                lift_state[idx] = max_people_in_wagon
                people_waiting -= seats_free
            else:
                lift_state[idx] += people_waiting
                people_waiting = 0

    empty_seats = len(lift_state) * max_people_in_wagon - sum(lift_state)
    lift_state = ' '.join(list(map(str, lift_state)))
    if no_more_people_in_queue and empty_seats > 0:
        print('The lift has empty spots!')
        print(lift_state)
    elif (not no_more_people_in_queue) and empty_seats == 0:
        print(f'There isn\'t enough space! {people_waiting} people in a queue!')
        print(lift_state)
    elif no_more_people_in_queue and empty_seats == 0:
        print(lift_state)


# Driver code
if __name__ == '__main__':
    # function call
    the_lift()
