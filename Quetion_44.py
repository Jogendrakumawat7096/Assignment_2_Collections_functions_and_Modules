'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
'''

import itertools

data = {'1': ['a','b'], '2': ['c','d']}

for combo in itertools.product(*data.values()):
    print(''.join(combo))