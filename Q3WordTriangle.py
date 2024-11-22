# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON
print('This program takes a word or a sentence you enter and prints it, one letter at a time.\n'+'It will look like a word triangle.')
txt=input()
for x in range(len(txt)):
    print(txt[0:x+1])