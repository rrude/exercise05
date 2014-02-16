# Write a program, lettercount.py, that opens a file named on the command line and counts how many times each letter occurs in that file. Your program should then print those counts to the screen, in alphabetical order. 
#open file, read file
#print the counts to the screen in alphabetical order
#use dictionary


from sys import argv
#argv allows set variables for your program 
script, filename = argv

txt = open(filename)
#read with argument of 1 reads it character by character, but 
filetext = txt.read()
txt.close()



d = {}

for char in filetext:
    char1 = char.lower()
    if ord(char1) >= ord("a") and ord(char1) <= ord("z"):
        if d.get(char1):
            d[char1] += 1
        else:
            d[char1] = 1   
          

for key in sorted(d.keys()):
    print "%s : %d" % (key, d[key])


 #for spark comment above and use this below
# for key in sorted(d.keys()):
#     print "%d" % (d[key])   



