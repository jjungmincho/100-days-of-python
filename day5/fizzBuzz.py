for number in range (1, 101):
  if number % 3 == 0 & number % 5 == 0:
    #Divisible by 3
    print("FizzBuzz")
  elif number % 5 == 0:
    #Divisible by 5
    print("Fizz")
  elif number % 3 == 0:
    #Divisible by 3 and 5
    print("Buzz")
  else:
    print(number)
