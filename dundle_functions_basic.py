class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

# Usage
book1 = Book("Python Basics", 200)
book2 = Book("Advanced Python", 300)

print(book1)        # Triggers __str__: 'Python Basics' (200 pages)
print(len(book1))   # Triggers __len__: 200
print(book1 + book2) # Triggers __add__: 500
