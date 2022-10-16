# Factorial:
def fact(n):
   if n == 1:
      return 1
   return n * fact(n - 1)

print(fact(10))

# Recursive Power:
def recursive_power(x, y):
   result = 1
   if y == 0:
      return result
   result = x * recursive_power(x, y - 1)
   return result
