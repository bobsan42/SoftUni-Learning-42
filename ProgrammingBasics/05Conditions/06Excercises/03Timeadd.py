hr = int(input())
mins = int(input())
nn = mins + 15  # minutes
oo = nn // 60
pp = nn % 60
hr = hr + oo
if hr >= 24:
    hr = hr-24
# if pp>10:
#     pp='0' & pp
print(f'{hr}:{pp:02d}')
