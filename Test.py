#1
num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in the second number: "))

if (num1 > num2):
    print (f"The greater number is {num1}")
elif (num2 < num1):
    print (f"The greater number is {num2}")
else:
    print (f"{num1} and {num2} are equal")
    
#2
num = int(input("Please type in a number: "))

if (num % 3 != 0 and num % 5 != 0 ):
    print ("Stop")
elif (num % 5 == 0 and num % 3 == 0):
    print ("FizzBuzz")
elif (num % 3 == 0):
    print ("Fizz")
elif (num % 5 == 0):
    print ("Buzz")

#3
Username = input("Please enter your username: ")
Pass = input("Please enter your password: ")

if (Username == "user123" and Pass == "securepassword"):
    print ("Access granted!")

else:
    print ("Incorrect password or username!")
