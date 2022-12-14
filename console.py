import pdb
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("JK Rowling")
author_repository.save(author_1)

book_1 = Book("Harry Potter and Philosophers Stone", author_1)
book_repository.save(book_1)

book_2 = Book("Harry Potter and the Chamber of Secrets", author_1)
book_repository.save(book_2)

# result = book_repository.select_all()
# print(result[0].__dict__)

# for book in result:
#     print(book.__dict__)
#     print(book.author.__dict__)

# book_repository.delete(1)