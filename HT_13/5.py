"""
5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).
"""


class SchoolLibrary(object):
    number_of_books = 0
    number_of_students = 0
    book = []
    students = []

    def __init__(self, name, title=None, year_of_publication=None, short_description=None):
        self.name = name
        self.title = title
        self.year_of_publication = year_of_publication
        self.short_description = short_description
        if title is not None:
            SchoolLibrary.number_of_books += 1
            self.book.append([self.name, self.title])
        else:
            SchoolLibrary.number_of_students += 1
            self.students.append(self.name)

    def information(self):
        for k, v in self.__dict__.items():
            if v is not None:
                print(k, v)


a = SchoolLibrary(
    'Swaroop Chitlur',
    'A Byte of Python',
    2012,
    '"A Byte of Python" is a free book on programming using the Python language',
)
a1 = SchoolLibrary(
    'Mark Lutz',
    'Learning Python',
    2019,
    'The first volume of the fifth edition of the legendary book "Learn Python"',
)
b = SchoolLibrary('school student')
b1 = SchoolLibrary('school student1')
b2 = SchoolLibrary('school student2')


# b.information()


def available_books():
    for name, title in SchoolLibrary.book:
        print(name, '-', title)


def library_students():
    for name in SchoolLibrary.students:
        print(name)


def School_lib():
    """Displays basic information about the library"""
    print('School library')
    print(
        f'''The number of books in the library is {SchoolLibrary.number_of_books} books
Number of library users {SchoolLibrary.number_of_students}
-------------------------------------
To view available books, enter 1
List of library visitors, enter 2
        ''')
    choice = input('Your choice: ')
    if choice == '1':
        available_books()
    elif choice == '2':
        library_students()


School_lib()
