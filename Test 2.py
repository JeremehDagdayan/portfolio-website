#1

my_list = [20,40,60,80,100, 120]

my_list = my_list.copy()
print(my_list)
my_list.insert(1,30)
print(my_list)
my_list.append(140)
print(my_list)
my_list.remove(40)
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
my_list.append(200)
print(my_list)


#2

def converter_m(gallon):
    gallon = int(input("Give me a number in gallons and I will convert it to liters: "))
    liters = gallon * 3.78541
    return liters

print(converter_m(1))


#3

def all_in_one():
    done = 'n'
    while done != 'y':
        my_list = []
        for _ in range(3):
            my_list.append(int(input("Enter 3 numbers: ")))
        print (f"Your list is {my_list}")
        for i in range (3):
            if my_list[i] == -1:
                my_list[i] = 99
        print(f"Now your list is {my_list}")
        done = input("If you would like ot stop write 'y': ").lower()
        
all_in_one()
