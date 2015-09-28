authorr={}
print "1 - Enter book"
print "2 - Find book"
menue = int(raw_input("Choose any number"))

def enterbook():
    global authorr
    for i in range(2):

        Title = raw_input("Enter book Title")
        Author = raw_input("Enter author")
        authorr[Title] = Author
    return authorr

def findbook():
    #title = enterbook()
    Title = raw_input("Enter book Title")
    author = authorr[Title]
    return author

if menue==1:
    enterbook()

elif menue==2:
    print findbook()


#print findbook()