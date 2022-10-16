text = input()

while True:
    try:
        times = int(input())
        break
    except ValueError:
        print("Variable times must be an integer")

print(text * times)
