# This script generates a list of random integers between 1 and 50, sorts it, and prints the sorted list.

import random
list_size = int(input("Enter the number of random elements: "))
random_list = [random.randint(1, 50) for _ in range(list_size)]
random_list.sort()
print("Sorted List:", random_list)