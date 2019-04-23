#Raul Rivera
#4/22/19


f = open("testText.txt", "r")
newf = open("NewtestText.txt","w")

counter = 1
for line in f:
    if counter % 2 !=0:
        newf.write(line)
        counter +=1




f.close()
newf.close()
