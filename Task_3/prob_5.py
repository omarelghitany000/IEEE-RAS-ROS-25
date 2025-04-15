#This script takes a set of integers from user input, adds a new number, and prints the updated set (ensuring no duplicates).

my_set = set(map(int, input("Enter set elements separated by space: ").split()))
my_set.add(int(input("Enter a number to add to the set: ")))
print(my_set)  # Print the set without duplicates