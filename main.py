from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///sqlalchemy_tryouts.db")

# Create a declarative base class
Base = declarative_base()

# Define the Book model
class Book(Base):
    __tablename__ = 'Books'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(100))

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', genre='{self.genre}')>"

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a book
new_book = Book(title="Atomic Habits", author="James Clear", genre="Life")
session.add(new_book)
session.commit()

# Select all books
all_books = session.query(Book).all()
print(all_books)

# Select book with a specific author name
get_book_by_author = session.query(Book).filter_by(author="James Clear").first()
print(get_book_by_author)

# Select a book with title starting with 'at'
get_book_by_title = session.query(Book).filter(Book.title.like('at%')).all()
print(get_book_by_title)

# Close the session
session.close()