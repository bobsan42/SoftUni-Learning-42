from math import floor

# •	На първия ред са необходимите часовете – цяло число в интервала [0 ... 200 000]
hrs = int(input())
# •	На втория ред са дните, с които фирмата разполага – цяло число в интервала [0 ... 20 000]
days = int(input())
# •	На третия ред е броят на служителите, работещи извънредно – цяло число в интервала [0 ... 200]
emp = int(input())

hrs_available = 8 * days * 0.90
hrs_extra = emp * (days * 2)
total_hrs = floor(hrs_available + hrs_extra)
if total_hrs >= hrs:
    print(f'Yes!{total_hrs - hrs} hours left.')
else:
    print(f'Not enough time!{hrs - total_hrs} hours needed.')
