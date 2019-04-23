#Raul Rivera
#4/22/19
#Open a file and gives a count of occurances for each word.
Textd ={}
f = open("testText.txt", "r")

def buildTextd(words):
    for x in words:
        if x not in Textd:
            Textd[x] = 1
        else:
            Textd[x] = Textd[x] + 1

for line in f:
    w = line.split()
    buildTextd(w)

print (Textd)
f.close()

