#virtualna biblioteka
#CRUD
#Dodaj knjigu
#Izlistaj knjigu
#Obrisi knjigu

books = []

def add_book (book_name, book_author) :
    books.append({"name": book_name, "author": book_author})

def find_book_by_name(name):
    for book in books:
        if book["name"] == name :
            return book

add_book("Harry Potter 1", "J K Rowling")
add_book("Harry Potter 2", "J K Rowling")


book= find_book_by_name("Harry Potter 2")
print(book)

def delete_book_by_name (book_name) :
    search_book = find_book_by_name(book_name)
    if search_book is None :
        print("Book not found")
    else:
        books.remove(search_book)

delete_book_by_name("Harry Potter 1")