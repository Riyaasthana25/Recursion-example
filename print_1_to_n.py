def printNumber(n):
  if n > 0:
    printNumber(n - 1)
    print(n, end = ' ')
#driver code 
n = int(input("Enter a number:"))
printNumber(n)
