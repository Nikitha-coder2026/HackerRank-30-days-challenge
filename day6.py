# -----------HackerRank 30 days challenge-------------
# -----------Day06: Operators, Strings and Loops----------

#Enter your code here. Read input from STDIN. Print output to STDOUT.
t = int(input().strip())

for _ in range(t):
    s = input().strip()
    even_indexed = ""
    odd_indexed = ""

    # Iterate each character through index.
    for i in range(len(s)):
        if i % 2 == 0:
            even_indexed += s[i]
        else:
            odd_indexed += s[i]
    print(f"{even_indexed} {odd_indexed}")
