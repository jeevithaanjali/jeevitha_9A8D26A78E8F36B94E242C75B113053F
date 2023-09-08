

def fact(n):


  if(n==0):
    return 1
  else:
    return n*fact(n-1)
num=int(input("enter the number:"))
print("the factorial value of",num,"is",fact(num))