#Task 1
speed = int(input("Enter the speed of the car in m/h: "))
print (f"The distance the car will travel in 4 hours: {speed*4} miles")
print (f"The distance the car will travel in 6 hours: {speed*6} miles")
print (f"The distance the car will travel in 10 hours: {speed*10} miles")

#I asked for user input and put it into a variable. I put it in f string so I can call on it later. 
#I multiplied what the speed is to how long they were driving for.

#Task 2
while True:
    date = int(input("Enter a number from 1 to 7: "))
    if date ==  1:
        print("1 is Monday")
    elif date ==  2:
        print("2 is Tuesday")
    elif date ==  3:
        print("3 is Wednseday")
    elif date ==  4:
        print("4 is Thursday")
    elif date ==  5:
        print("5 is Friday")
        break
    elif date ==  6:
        print("6 is Saturday")
        break
    elif date ==  7:
        print("7 is Sunday")
        break
    else:
        print("You entered the wrong number please try again")
    
#I asked for the users input ot put it into the "date" variable 
#I made a loop using while true: and I put a break on numbers 1 through 7 to end the code if they get there.
#If they chose numbers that were not in the range the code would keep repeating cause of while true.

#Task 3
my_list = []

def count_A(x_str):
    my_list=x_str.split()
    return my_list

count_A(my_list)