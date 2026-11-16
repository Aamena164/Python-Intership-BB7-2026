library={
    101: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald","copies": 5},
    102: {"title": "To Kill a Mockingbird", "author": "Harper Lee","copies": 3},
    103: {"title": "1984", "author": "George Orwell","copies": 4}
}


book_id=102

if book_id in library:
    library[book_id]["copies"]=library[book_id]["copies"]-1
    print(library)
else:
    print("Book not found")
         
        