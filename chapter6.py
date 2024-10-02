print("puzzle 1\n")
for i in range(10):
  print("*", end = "")
print("\n")




print("Puzzle 2")
for row in range(5): 
  print("*", end=" ")
print()
for row in range(10):
  print("*",end=" ")
print()
for row in range(20): 
  print("*", end=" ")
print()







print("Puzzle 3")

for row in range(10):
  for column in range(10):
    print("*", end = " ")
  print()








print("\n Puzzle 4")
for row in range(10):
  for column in range(5):
    print("*", end = " ")
  print()







print("\n Puzzle 5")
for row in range(5):
  for column in range(20):
    print("*", end = " ")
  print()














print("\n puzzle 6")
for row in range(10):
  for column in range(10):
    print(column, end = " ")
  print()









print("\n puzzle 7")
for row in range(10):
  for column in range(10):
    print(row, end = " ")
  print()

print("\n puzzle 8")
for row in range(10):
  for column in range(row+1):
    print(column, end = " ")
  print()

print("\n puzzle 9")
for row in range(10):
  for j in range(row):
    print (" ",end=" ")
  for j in range(10-row):
    print (j,end=" ")
  print()

print("\n puzzle 10")
for row in range(1, 10):
  for column in range(1, 10):
    if len(str(row * column)) == 1: 
      print(" ", row* column, end = " ")
    else: 
      print("", row*column, end = " ")
  print()





#problem # 11
for row in range(1, 10):
   for column in range(10,row, -1):
     print(" ", end = " ")
   for column in range(0,row):
     print(column+ 1, end = " ")
   for column in range(row-1, 0, -1):
      print(column, end = " ")
   print()
print(" ")




# problem 12
for row in range(1, 10):
  for column in range(10,row, -1):
    print(" ", end = " ")
  for column in range(0,row):
    print(column+ 1, end = " ")
  for column in range(row-1, 0, -1):
     print(column, end = " ")
  print()
for row in range(9, 1, -1):
  print("    ", end = "")
  for column in range(row, 9, 1):
    print(" ", end = " ")
  for column in range(1, row):
    print(column, end = " ")
  for column in range(row-2, 0, -1):
    print(column, end = " ")
  print()




print("let's do the lab")
print("problem 1")
start = 10
for row in range(10):
  for column in range(row):
    print(start, end = " ")
    start +=1
  print()


print("***problem 2****")
n = input("how big is your box? \n")
n = int(n)
for row in range(0, n):
  print("o", end = "")
print()
for row in range(0, n-2):
  print("o", end = "")
  for column in range(0, n-2):
    print(" ", end = "")
  print("o")
for row in range(0,n):
  print("o", end="")
print()




print("***problem 3***")
n = input("how big is your box?\n")
n = int(n)
n = 2*n -1
for row in range(1,n+1,2):
    for column in range(row, n+1,2):
        print(column, end = " ")
    print(" "*(2*row-2), end = "")
    for column in range(n, row-1, -2):
        print(column, end = " ")
    print()
for row in range(n, 0, -2):
    for column in range(row, n+2, 2):
        print(column, end = " ")
    print(" "*(2*row-2), end = "")
    for column in range(n,row-1,-2): 
        print(column, end = " ")
    print()
