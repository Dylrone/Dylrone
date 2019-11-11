# Have user ask for file in CSC 2280
# Find Word Count for file
# Find UNIQUE Word Count for File

def counter():
    filenm = input("What file in CSC 2280 do you wish to open: ")
    all_words = []
    nme = open(filenm, 'r')
    for line in nme:
        words = line.split()
        for word in words:
            all_words = all_words + [word.lower()]
    nme.close()

    uniquewords = list(set(all_words))
    print("Total words:", len(all_words))
    print("Total unique words:", len(uniquewords))
    uniquewords.sort()
    for word in uniquewords:
        print(word)
                           

    
          
    

counter()
