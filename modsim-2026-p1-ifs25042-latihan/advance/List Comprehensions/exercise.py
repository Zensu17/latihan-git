numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [23, 123, 22, 45, 322, 12, 3, 7, 2, 1,] 
print(newlist)
newlist = [int(x) for x in numbers if x > 0]
print(newlist)