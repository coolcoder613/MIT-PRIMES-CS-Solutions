
"""MIT PRIMES Computer Science Problem #1
Description of the program:
This program inputs a string of digits (up to 30 digits in length), and finds all ways to partition the digits. In addition, it finds the partition which produces the greatest number of prime factors.

Instructions for how to run the code:
When prompted, enter the string of digits of your choice, and the program will output the optimal partition."""

import math
num = input("Enter a string of digits: ")
intnum = int(num)

def split(word): 
    '''This function splits the string that was taken as an input into its constitutional digits. The result is a list with each digit as a term in the list.'''
    return [char for char in word]
from itertools import combinations 
num_string = split(num) #The number string that was inputted is now being split, so it can be grouped off into partitions later on
length = len(num_string)

def combo(arr, r): 
    '''This function finds the number of permutations that can be done for a list of numbers'''
    return list(combinations(arr, r)) 

rangeValues = [] #Making a list which has all of the values from 1 to n, where n is the length of the inputted string, so that it can be passed into the combo function.
partitionList = [] #Making a list of indices by which num_string will be split

for i in range (1,length+1):
    rangeValues.append(i)
for i in range(1,length):
    partitionList+=(combo(rangeValues, i))
joinedFactors = [] #Making a list to store all of the prime factors from the partitions after

def get_prime_factors(number):
    '''The function finds all of the prime factors of a number and outputs them as a list'''
    prime_factors = []

    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i

    if number > 2:
        prime_factors.append(int(number))

    return prime_factors

factorList = []
list_of_partitions = []

for x in (partitionList):
    partitions = []
    split_ratio = list(x) 
    res = [num_string[i : j] for i, j in zip([0] + split_ratio, split_ratio + [None])] 
    for i in res:
        part = "".join(i)
        partitions.append(part)
        while("" in partitions): 
            partitions.remove("") #removing any empty entries in the list of partitions
    for i in partitions:
        joinedFactors += get_prime_factors(int(i))
        factorList.append(joinedFactors)
        list_of_partitions.append(partitions)
    joinedFactors = []

factor_list_modified = [] #Creating a factor list which is devoid of all the repeats
for i in factorList: 
    if i not in factor_list_modified: 
        factor_list_modified.append(i)

partitions_list_modified = [] #Creating a partition list which is devoid of all the repeats
for i in list_of_partitions: 
    if i not in partitions_list_modified: 
        partitions_list_modified.append(i)

length_list = [] #Creating a list which contains all the lengths of the prime number lists
for i in factor_list_modified:
    length_list.append(len(i))

max_factors = max(length_list) #Finding the index of the partition which yielded the longest list of prime factors
index_of_max = length_list.index(max_factors)

optimal_partition = partitions_list_modified[index_of_max] #Using max_factors to find the optimal parition

print(optimal_partition, max_factors) #Printing the results!

"""1. This program always gives the correct answer, because it goes through all of the partitions, and finds all fo the prime factors for each element in the partition.
It then makes a list of the lengths of the prime factor sequences for each of the partitons. Afterwards, it goes through the list of lengths, and returns the partition
which corresponds to the sequence with greatest length.

2. The worst case effiency is for strings of length 15 and greater. For these strings, it takes quite a while for the answer to be outputted.

3. The expected result is an answer within 5 seconds of running. However, in the case of some larger strings, the program takes quite a while to give the answer.

4. In order to make my code run faster, I used the combinations function. I then used the output from that function as the input for the split function,
which took the inputted combinations, and used them as indices to split the list at specific locations. This is a fast way of making sure that all of the partitions are present,
instead of having to identify the indices of each split,for which the alck of efficiency would definitely be apparent for longer strings. Lastly, at the end, repeats are removed, for added efficiency."""
