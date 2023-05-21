def printNumber(n):
  if n > 0:
      print(n, end = ' ')
      printNumber(n - 1)
    
n = int(input("ENter the number"))
printNumber(n)
