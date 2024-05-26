#!/usr/bin/python3

if __name__== "__main__":
  
    import calculation as calc

    a = 4 #use this variable as a first argument to call a function 
    b = 2 #use this variable as a second argument to call a function

    print(f"{a} + {b} = {calc.add(a, b)}")
    print(f"{a} - {b} = {calc.sub(a, b)}")
    print(f"{a} * {b} = {calc.mul(a, b)}")
    print(f"{a} / {b} = {calc.div(a, b)}")
