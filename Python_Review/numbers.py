class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f""""{self.title}", is a book written by {self.author}, and is {self.pages} long."""

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Book is destroyed")

b = Book("Python", "Ian", 200)
print(b)
print(len(b))
del b
