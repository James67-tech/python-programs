symbol = '*'

for i in range(5):
    print(" " * (4 - i), end="")
    for x in range(i+1):
        print(symbol, end=" ")
    print()
    