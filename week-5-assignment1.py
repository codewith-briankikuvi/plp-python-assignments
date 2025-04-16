# Base Class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.__pages = pages  # Encapsulated attribute

    def get_pages(self):
        return self.__pages  # Getter for encapsulated pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

# Subclass: AudioBook inherits from Book
class AudioBook(Book):
    def __init__(self, title, author, pages, narrator):
        super().__init__(title, author, pages)
        self.narrator = narrator

    # Polymorphism: Overriding the read method
    def read(self):
        print(f"Listening to '{self.title}' narrated by {self.narrator}.")

# Using the classes
book1 = Book("The Alchemist", "Paulo Coelho", 208)
book1.read()
print(f"Page Count: {book1.get_pages()}")

print()

audio1 = AudioBook("The Alchemist", "Paulo Coelho", 208, "Jeremy Irons")
audio1.read()
print(f"Page Count (from audiobook info): {audio1.get_pages()}")
