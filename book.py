

class Book(object):
    def __init__(self,title,author):
        self.title=title
        self.author=author
        #shelf[self.Title]=self.Author

    def __repr__(self):
        return self.title + self.author
        #return shelf


class Shelf(object):
     def __init__(self):
         self.books=[]

     def add(self,book):
        self.books.append(book)

     def find(self,title):
         for book in self.books:
            if book.title==title:
                return book

book_shelf=Shelf()

def showmenue():
    print "1 - Enter book"
    print "2 - Find book"
    menue = int(raw_input("Choose any number"))
    if menue==1:
        enterbook()
    elif menue==2:
        findbook()

def enterbook():
    title = raw_input("Enter book Title")
    author = raw_input("Enter author")
    book = Book(title,author)
    book_shelf.add(book)
    showmenue()



def findbook():
    title = raw_input("Enter book Title")
    book = book_shelf.find(title)
    print book
    showmenue()




showmenue()



