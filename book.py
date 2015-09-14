authorr={}

def enterbook():

    for i in range(2):

        Title = raw_input("Enter book Title")
        Author = raw_input("Enter author")
        authorr[Title] = Author
    return authorr

def findbook():
    title = enterbook()
    Title = raw_input("Enter book Title")
    author = title[Title]
    return author


print findbook()
