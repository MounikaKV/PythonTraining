def top10_perfect_squares():
    n = 1
    while (n <= 10):
        sq = n*n
        yield sq
        n += 1

values = top10_perfect_squares()

for i in values:
    print(i)
