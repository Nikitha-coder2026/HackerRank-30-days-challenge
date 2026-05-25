# -------------HackerRank 30 days challenge-------------
# -------------Day07: Arrays----------------------------

if __name__ == '__main__':
   n = int(input().strip()) # Reads the size of an array.

   arr = list(map(int, input().rstrip().split()))

   print(*(arr[::-1])) # print reversed array
