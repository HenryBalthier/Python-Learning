
x = [
  [1,2,3],
  [4,5,6]
]

a = list(map(list, zip(*x)))
print(a)

a = list(map(list, zip(*x[::-1])))
print(a)

a = list(map(list, zip(*x)))[::-1]
print(a)
