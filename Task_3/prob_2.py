# This script asks for the user's name and prints a personalized greeting.my_list = 
# list(map(int, input("Enter list elements separated by space: ").split()))

my_list = list(map(int, input("Enter list elements separated by space: ").split()))
my_list.append(int(input("Enter a number to add: ")))
my_list.remove(int(input("Enter a number to remove: ")))
print(my_list)  