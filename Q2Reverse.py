# Create a program that will accept a word and output the word one letter at a time in reverse.
print('This program reverses a word or a sentence you enter, one letter at a time.')
txt=input()
backwards=''
for x in range(len(txt)):
    backwards=backwards+txt[len(txt)-1-x]
    print(backwards)