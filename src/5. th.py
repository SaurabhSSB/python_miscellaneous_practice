"""
Write a Python program to extract and print only the names from a given list of full names with titles. The titles (Mr. or Ms.) should be removed from the output.
lnames = ['Mr.Manish', 'Ms.Ananya', 'Ms.Jyotika', 'Mr.Cache']
Expected Output:
['Manish', 'Ananya', 'Jyotika', 'Cache']

A program that traverses a list and return the list after removing the titles from the name.
"""

lnames: list = ['Mr.Manish', 'Ms.Ananya', 'Ms.Jyotika', 'Mr.Cache']
list_1: list = []

for i in lnames:
    list_1.append(i[3:])

print(list_1)