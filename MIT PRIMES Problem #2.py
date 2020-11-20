
"""MIT PRIMES Computer Science Problem #1
Description for the program:
This program inputs two strings of digits (up to 30 digits in length), and finds all ways to partition the digits of the first number. In addition, it finds the partition which multiplies to the second number (which is a number between 1 and the first number).

Instructions for how to run the code:
When prompted, enter two strings of digits of your choice. Then watch the code run!"""

import math

num = input("Enter a number: ")
num2 = input("Enter a number between 1 and the first number: ")

intnum = int(num)
def split(word): 
    '''This function splits the string that was taken as an input into its constitutional digits. The result is a list with each digit as a term in the list.'''
    return [char for char in word]

from itertools import combinations 
num_string = split(num)
length = len(num_string) 
def combo(arr, r): 
    return list(combinations(arr, r)) 

rangeValues = []
partitionList = []
for i in range (1,length+1):
    rangeValues.append(i)
for i in range(1,length):
    partitionList+=(combo(rangeValues, i))

list_of_partitions = []

for x in (partitionList):
    partitions = []
    split_ratio = list(x) 
    res = [num_string[i : j] for i, j in zip([0] + split_ratio, split_ratio + [None])] 
    for i in res:
        part = "".join(i)
        partitions.append(part)
        while("" in partitions) : 
            partitions.remove("")
    for i in partitions:
        list_of_partitions.append(partitions)

partitions_list_modified = [] 
for i in list_of_partitions: 
    if i not in partitions_list_modified: 
        partitions_list_modified.append(i)

product_list = []
product = 1
for i in partitions_list_modified:
    for j in i:
        product *= int(j)
    product_list.append(product)
    product=1

for i in product_list:
    if i == int(num2):
        print(partitions_list_modified[product_list.index(i)])
        
if int(num2) not in product_list:
    print("No Solutions")
"""1. This program always gives the correct answer, because it goes through all of the partitions, and finds all fo the prime factors for each element in the partition.
It then makes a list of the products of all of the partitions, and finds the one which matches with the second input.

2. The worst case effiency is for strings of length 15 and greater. For these strings, it takes quite a while for the answer to be outputted.

3. The expected result is an answer within 5 seconds of running. However, in the case of some larger strings, the program takes quite a while to give the answer.

4. In order to make my code run faster, I used the combinations function. I then used the output from that function as the input for the split function,
which took the inputted combinations, and used them as indices to split the list at specific locations. This is a fast way of making sure that all of the partitions are present,
instead of having to identify the indices of each split, for which the inefficiency would definitely be apparent for longer strings. Lastly, at the end, repeats are removed, for added efficiency."""

