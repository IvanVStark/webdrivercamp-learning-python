#!/usr/bin/python3

def fizz_buzz():

    for a in range (1, 101):

        if a%3==0 and a%5==0:
            print("FizzBuzz", end=" ")
        elif a % 3 == 0:
            print("Fizz",     end=" ")
        elif a % 5 == 0:
            print("Buzz",     end=" ")
        else:
            print(a, end=" ")
                    
fizz_buzz()
