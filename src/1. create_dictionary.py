"""
Write a Python program to create a dictionary using the given lists.
names = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
ages = [24, 21, 23, 20]
Use the provided lists to create a dictionary where the names act as keys and ages as values.
Expected output:
{'MANISH': 24, 'SAMARTH': 21, 'AYUSH': 23, 'ANANYA': 20}

A program that traverses two lists and display them in dictionary format.
"""

names: list[str] = ["MANISH", "SAMARTH", "AYUSH", "ANANYA"]
ages: list[int] = [24, 21, 23, 20]
dict_1: dict= dict(zip(names,ages))

print(dict_1)