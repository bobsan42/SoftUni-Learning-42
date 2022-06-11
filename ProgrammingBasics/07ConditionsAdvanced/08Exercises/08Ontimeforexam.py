exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

min_exam = exam_hour * 60 + exam_min # convert time to minutes only
min_arrive = arrive_hour * 60 + arrive_min # convert time to minutes only
# not checking for midnight overflow

diff = abs(min_exam - min_arrive)
arrival = 'On time'

if min_arrive > min_exam:
    arrival = 'Late'
elif min_arrive < min_exam - 30:
    arrival = 'Early'
h_diff = diff // 60
m_diff = diff % 60
output_line_2 = ''

if diff > 0:
    if h_diff > 0:
        output_line_2 = f'{h_diff}:{m_diff:02d} hours'
    else:
        output_line_2 = f'{m_diff} minutes'

    if min_exam < min_arrive:
        output_line_2 = output_line_2 + ' after the start'
    else:
        output_line_2 = output_line_2 + ' before the start'

print(arrival)
if output_line_2 != '':
    print(output_line_2)
