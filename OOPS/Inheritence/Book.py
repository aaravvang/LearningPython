"""Create a class named Book with properties title, author, and year. Create a subclass named EBook that inherits from the Book class, and has an additional property file_size. Add a method get_size() that returns the size of the eBook file."""


class Book:
  def title(self):
    print("Sherlock Holmes")
  def author(self):
    print("Doyle")
  def year(self):
    print(1887)

class EBook(Book):
  file_Size = 30
  def get_size(self):
    return self.file_Size

book = EBook()
book.title()
book.author()
book.year()
print(book.get_size())