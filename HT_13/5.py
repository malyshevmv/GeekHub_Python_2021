"""
5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію)
"""


class SchoolLibrary(object):
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books

    def print_list(self):
        for book in self.list_of_books:
            print(book)

    def gives_the_book(self, book):
        if book in self.list_of_books:
            self.list_of_books.remove(book)
            print(f'You got the book {book} do not forget to return it')
        else:
            print('The book is not in the library')

    def add_a_book(self, book):
        self.list_of_books.append(book)
        print('Thank you for returning the book')

    def __len__(self):
        return len(self.list_of_books)


class Student(object):
    def __init__(self, name):
        self.name = name
        self.number_of_books = []

    def to_take_the_book(self):
        self.book = input('Enter book: ')
        self.number_of_books.append(self.book)
        return self.book

    def return_the_book(self):
        self.book = input('Enter book: ')
        self.number_of_books.remove(self.book)
        return self.book

    def print_lst(self):
        if self.number_of_books:
            for book in self.number_of_books:
                print(book)
        else:
            print('Your book list is empty')


def menu():
    lib = SchoolLibrary(['book1', 'book2', 'book3'])
    st = Student('student1')
    print('\t', 'Welcome to the school library!')
    while True:

        print(f'''
The school library has {len(lib)} books
        
To view which books are in the library, enter 1
To get a book, enter 2
To return a book, enter 3
To view a list of books you have, enter 4
To exit, enter 5
    ''')
        choice = int(input('Your choice: '))
        if choice == 1:
            SchoolLibrary.print_list(lib)
        elif choice == 2:
            lib.gives_the_book(st.to_take_the_book())
        elif choice == 3:
            lib.add_a_book(st.return_the_book())
        elif choice == 4:
            st.print_lst()
        elif choice == 5:
            return


menu()