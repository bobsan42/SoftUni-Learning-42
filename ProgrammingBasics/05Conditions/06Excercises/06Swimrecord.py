# for i in range(0, 10000, 10):
#     print(f'{i: 5d}: ',end='')
#     print(f'{i%5==0}: ', end='')
#     print(f'{i % 5}')

c_record = float(input())
dist = float(input())
delay = (dist // 15) * 12.5
speed = float(input())
t_time = dist * speed + delay
if t_time < c_record:
    print(f'Yes, he succeeded! The new world record is {t_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {(t_time - c_record):.2f} seconds slower.')
