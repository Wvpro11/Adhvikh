

def myCalculator():
  symbol=input(("Which operator do you want to use:Addition,Subtraction,Multiplication,Division,or Exponents :"))
  if symbol=="addition":
    Addition=input(("1:"))
    Addition2=input(("2:"))
    sum=int(Addition)+int(Addition2)
    print(sum)
  if symbol== "subtraction":
    Sub1=input(("1:"))
    Sub2=input(("2:"))
    sum=int(Sub1)-int(Sub2)
    print(sum)
  if symbol== "multiplication":
    Mult1=input(("1:"))
    Mult2=input(("2:"))
    sum=int(Mult1)*int(Mult2)
    print(sum)
  if symbol== "division":
    Div1=input(("1:"))
    Div2=input(("2:"))  
    sum=int(Div1)/int(Div2)
    print(sum)
  if symbol == "exponents":
    number=input(("1:"))
    Power=input(("2:"))
    sum=int(number)**int(Power)
    print(sum)


myCalculator()

