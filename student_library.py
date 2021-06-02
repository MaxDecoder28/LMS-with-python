# LMS library management system


class library:

    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayavailablebooks(self):
        print("Books present in this library are:-")
        for book in self.books:
            print("*"+book)

    def borrowbook(self, bookname):
        if bookname in self.books:
            print(
                f"You have been issued {bookname}. Please it keep safe and return it within 30 days.")
            self.books.remove(bookname)
            return True

        else:
            print("Sorry, This book is either not available has already been issued to someone else. Please wait until the book is available.")
            return False

    def returnbook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning or donating this book ! Hope you enjoyed reading it! Have a great day ahead.")


class Student:

    def requestbook(self):
        self.book = input("Enter the name of the book you want to borrow:-")
        return self.book

    def returnbook(self):
        self.book = input("Enter the name of the book you waant to return or donate a book:-")
        return self.book


if __name__ == "__main__":
    centralibrary = library(["Algorithms", "Django", "Clrs", "Python"])
    student = Student()
    # centralibrary.displayavailablebooks()

    while(True):
        welcomemsg = '''

=====Welcome to Central Library=====
Please choose an option:
1. List all the books.
2. Request a book
3. Add/Return  a book
4. Exit the library
        '''
        print(welcomemsg)
        a = int(input("Enter the choice:-"))
        if a == 1:
            centralibrary.displayavailablebooks()
        elif a == 2:
            centralibrary.borrowbook(student.requestbook())
        elif a == 3:
            centralibrary.returnbook(student.returnbook())
        elif a == 4:
            print("Thanks for using Central library! Have a great day ahead.")
            exit()
        else:
            print("Invalid Choice!")

