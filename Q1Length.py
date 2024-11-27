# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
print('This program will return the length of the word you type in.\n'+'To exit, enter "EXIT"')
while True:
    txt=input()
    if txt == 'EXIT':
        exit()
    print('Length of text: '+str(len(txt)))