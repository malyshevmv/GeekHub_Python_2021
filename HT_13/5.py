"""
5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).
"""


class Library(object):
    pass


class SchoolLibrary(Library):
    number_of_books = 0

    def __init__(self, title, author, year_of_publication, short_description):
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.short_description = short_description
        SchoolLibrary.number_of_books += 1

    def book_information(self):
        for k, v in self.__dict__.items():
            print(k, v)


a = SchoolLibrary('A Byte of Python',
                  'Swaroop Chitlur',
                  2012,
                  '"A Byte of Python" is a free book on programming using the Python language')

print(a.title)
print(a.short_description)
a.book_information()
