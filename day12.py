# -------------HackerRank 30 days challenge-------------
# -------------Day 12: Inheritance----------------------

class Person:
     def __init__(self, firstName, lastName, idNumber):
          self.firstName = firstName
          self.lastName = lastName
          self.idNumber = idNumber

     def printPerson(self):
         print("Name:", self.lastName + ",", self.firstName)
         print("ID:", self.idNumber)

class student(Person):
      # class constructor
      #
      # parameters:
      # firstName - A string denoting the persons first name.
      # lastName - A string denoting the persons last name.
      # id - An integer denoting the persons id number.
      # scores - An array of integers denoting the persons test scores.
      #
      # write your constructor here.
      def __init__(self, firstName, lastName, idNumber, scores):
           # use super() to initialize the parent(Person) class
           super().__init__(firstName, lastName, idNumber)
           self.scores = scores
      # Function Name: calculate
      # Return: A character denoting the grade.
      #
      # Write your function here.
      def calculate(self):
           # Average of scores
           average = sum(self.scores) / len(self.scores)

           if average >= 90:
              return 'O'
           elif average >= 80:
                return 'E'
           elif average >= 70:
                return 'A'
           elif average >= 55:
                return 'P'
           elif average >= 40:
                return 'D'
           else:
                return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list( map(int, input().split()) )
s = student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
