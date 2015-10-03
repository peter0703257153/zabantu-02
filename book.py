shelf={}


def showmenue():
    print "1 - Enter book"
    print "2 - Find book"
    menue = int(raw_input("Choose any number"))
    if menue==1:
        enterbook()
    elif menue==2:
        findbook()

def enterbook():
    Title = raw_input("Enter book Title")
    Author = raw_input("Enter author")
    shelf[Title] = Author
    showmenue()



def findbook():
    Title = raw_input("Enter book Title")
    author = shelf[Title]
    print author



showmenue()


