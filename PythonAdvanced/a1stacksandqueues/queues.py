from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")        # Terry arrives
queue.append("Graham")       # Graham arrives
queue.popleft()              # First leaves: 'Eric'
queue.popleft()              # Second leaves: 'John'
print(queue)                 # ['Michael', 'Terry', 'Graham']
