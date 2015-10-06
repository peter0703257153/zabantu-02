shelf={}

class Book(object):
    def __init__(self,Title,Author):
        self.Title=Title
        self.Author=Author
        shelf[self.Title]=self.Author

    def __repr__(self):
        #return self.Title + self.Author
        return shelf

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
    book = Book(Title,Author)
    showmenue()



def findbook():
    Title = raw_input("Enter book Title")
    print shelf[Title]
    showmenue()




showmenue()



