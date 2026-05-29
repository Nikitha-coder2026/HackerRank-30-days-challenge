# ------------HackerRank 30 days challenge-------------
# ------------Day 13: Abstract Classes-----------------

from abc import ABCMeta, abstractmethod

class Book(object, metaclass = ABCMeta):
      def __init__(self, title, author):
           self.title = title
           self.author = author
      @abstractmethod
      def display(): pass

# Write MyBook class
class MyBook(Book):
      # Step 1: The constructor
      def __init__(self, title, author, price):
           # Use super() to initialize title and author from the parent Book.
           super().__init__(title, author)
           # Add the unique price property for MyBook.
           self.price = price

      # step 2: Implement the abstract 'display' method.
      def display(self):
           print(f"Title: {self.title}")
           print(f"Author: {self.author}")
           print(f"Price: {self.price}")

title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
