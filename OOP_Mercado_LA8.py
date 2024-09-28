class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
libro = Book("48 Laws of Power", "Robert Greene")
print(f"{libro.title} and {libro.author}")
del libro.author
#print(f"{libro.title} and {libro.author}")
aklat = Book("The Subtle Art Of Not Giving A F", "Mark Manson")
print(f"{aklat.title} and {aklat.author}")