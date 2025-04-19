"""
Write a Python program to generate a nested list from a given list of names. Each element in the output list should be a dictionary, where the key is the name and the value is its length.
names = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
Expected Output:
[['MANISH', 6], ['SAMARTH', 7], ['AYUSH', 5], ['ANANYA', 6]]

A program that traverses a list and return a dictionary that contains the string element as key and the length of element as value.
"""

names: list = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
dict_1: dict = {}

for i in names:
    dict_1[i]= len(i)

print(list(dict_1.items()))


