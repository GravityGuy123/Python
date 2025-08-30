import datetime

# class Library:
#     list_of_books = []

#     def add_book(self, book: dict):
#         self.list_of_books.append(book)

#     def print_book(self):
#         print(self.list_of_books)


# Build a library for lending, of books while indicating the Author name, and Book Name

# class Library:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.list_of_books = []  # each library has its own book list

#     def add_book(self, book: dict) -> bool:
#         if not isinstance(book, dict):
#             print("Book must be a dictionary with details like title/author/year.")
#             return False
#         self.list_of_books.append(book)
#         return True

#     def remove_book(self, title: str) -> bool:
#         for book in self.list_of_books:
#             if book.get("title") == title:
#                 self.list_of_books.remove(book)
#                 return True
#         print(f"Book titled '{title}' not found.")
#         return False

#     def find_book(self, title: str) -> dict:
#         for book in self.list_of_books:
#             if book.get("title") == title:
#                 return book
#         return {}

#     def print_books(self) -> None:
#         if not self.list_of_books:
#             print("No books in the library yet.")
#         else:
#             print(f"📚 Books in {self.name}:")
#             for book in self.list_of_books:
#                 print(
#                     f"- {book.get('title')} by {book.get('author')} ({book.get('year')})"
#                 )



# ifenna = BankAccount("Ifenna")
# print(ifenna.check_balance())

# ifenna.deposit(50)
# print(ifenna.check_balance())

# ifenna.deposit(-550)  # will be rejected
# print(ifenna.check_balance())

# ifenna.withdraw(30)
# print(ifenna.check_balance())













class Book:
    def __init__(self, book: Book, title: str, author: str, num: int):
        self.title = title
        self.author = author
        self.num = num

class Library:
    def __init__(self) -> None:
        self.list_of_books = []
    
    def add_book(self, book: Book):
        self.list_of_books.append(book)

    def borrow_book(self, title: str, num: int = 1) -> str:
        # book = filter(lambda b: b.title == title, self.list_of_books)
        book: Book = list(filter(lambda b: b.title == title, self.list_of_books))[0]

        if not book:
            return f"Book with the title: -> {title} does not exist"
        if book.num < num:
            return f"You requested for {num} of books but we have {book.num} available"
        
        return f"Success: you borrowed {book.title} by {book.author}"
    
    def filter_book_by_title(self, title: str):
        for book in self .list_of_books:
            if title == book.title:
                return book
            return
        
    def print_books(self):
        print(self.list_of_books)





# def square():
#     a = input("Enter any number for a: ")
#     b = input("Enter any number for b: ")

#     a = int(a)
#     b = int(b)

#     print(a ** b)

# square()



# Types of Programming
# 1. Procedual programming (line by line)
# 2. Functional Programming (Python shines here)
# 3. Object Oriented Programming (OOP) 


# Object Oriented Programming (OOP)

class Person:
    def __init__(self, name: str, yob: int) -> None:
        self.name = name
        self.yob = yob
        self.school = None
        self.hobbies = []
        self.expires_at = datetime.date.today() + datetime.timedelta(seconds=30)
        self.is_expired = bool = datetime.date.today() > self.expires_at
        return
    
    def get_age(self) -> int:
        return datetime.date.today().year - self.yob
    
    def add_hobby(self, hobby: str) -> None:
        self.hobbies.append(hobby)

    def add_school(self, school: str) -> None:
        self.school = school
        return
    
    def print_info(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age}")
        print(f"School: {self.school}")
        print(f"Hobbies: {self.hobbies}")
        return

Person1 = Person("Ashioma", 2000)
Person1.add_hobby("Coding")
Person1.add_hobby("Reading")
Person1.print_info
Person1.school = "Unilag"


# Learn Date and Time Module in Python