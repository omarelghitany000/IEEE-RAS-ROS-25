#This script takes a tuple of integers from user input and prints the second element.

my_tuple = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
print(my_tuple[1])  