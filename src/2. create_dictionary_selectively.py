"""
Write a Python program to create a dictionary from a given list of names, where each name is mapped to a string containing only its vowels.
names = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]

Expected Output:
{'MANISH': 'AI', 'SAMARTH': 'AA', 'AYUSH': 'AU', 'ANANYA': 'AAA'}

A program that traverses a list and displays a dictionary with the vowels of the word written as value.
"""

names: list[str] = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
dict_1: dict = {}

for i in names:
    dict_1.update({i:""})
    for j in i.upper():
        if j in {"A","E","I","O","U"}:
            dict_1[i]+= j

print(dict_1)