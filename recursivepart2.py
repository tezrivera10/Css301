#Raul Rivera
#4/23/19
wordlist = ["Sunday", "Monday", "Tuesday"]
def reverse(words):
    return [words[-1]] + reverse(words[:-1]) if words else []
print (reverse(wordlist))
