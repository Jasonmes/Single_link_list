i = 1
for i in range(30):
    j = 0
    while j <= i:
        if i - j == 1:
            print("-\t", end="")
        else:
            print(" \t", end="")
        j += 1
    i += 1
    print()