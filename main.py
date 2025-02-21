def triangle(n):
   for i in range(1, n + 1):
       print('*' * i)
def reverse_triangle(n):
   for i in range(n, 0, -1):
       print('*' * i)
def diamond(n):
   for i in range(1, n + 1, 2):
       print(' ' * ((n - i) // 2) + '*' * i)
   for i in range(n - 2, 0, -2):
       print(' ' * ((n - i) // 2) + '*' * i)
# Change the value of n to adjust the size
n = 5
print("Triangle:")
triangle(n)
print("\nReverse Triangle:")
reverse_triangle(n)
print("\nDiamond:")
diamond(n)

