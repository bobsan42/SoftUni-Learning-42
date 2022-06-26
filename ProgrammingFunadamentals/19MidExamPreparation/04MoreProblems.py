# Programming Fundamentals Retake Exam - Part 1 - 6 January 2017
# Sino the Walker
# https://judge.softuni.org/Contests/Practice/Index/376#0

def time_add_seconds(init_time: str, seconds_to_add: int):
    time_limits = [24, 60, 60]
    numbers_list = list(map(int, init_time.split(':')))
    result = [None] * 3
    for idx in [2, 1, 0]:
        x = numbers_list[idx] + seconds_to_add
        seconds_to_add = x // time_limits[idx]
        x = x % time_limits[idx]
        result[idx] = f'{x:02}'
    return ':'.join(result)


def sino_the_walker():
    time_leaving = input()
    number_of_steps = int(input())
    seconds_per_step = int(input())
    time_arrival = time_add_seconds(time_leaving, number_of_steps * seconds_per_step)
    print(f"Time Arrival: {time_arrival}")


# Driver code
if __name__ == '__main__':
    # function call
    sino_the_walker()
