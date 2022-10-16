from collections import deque

queue = deque()
water_quantity = int(input())
name = input()
# add people to queue
command = input()
while command != "End":
    if "refill" in command:
        # increase liters
        # water_quantity += int(command.replace("refill",""))
    else:
        liters = int(command)
        if liters <= water_quantity:
            water_quantity -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f'{queue.popleft()} must wait')
    command = input()
print(f"{water_quantity} liters left")
