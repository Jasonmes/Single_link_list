while True:
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

    # for i in range(31, 0, -1):
    #     j = 1
    #     while j <= i:
    #         if i - j == 1:
    #             print("-\t", end="")
    #         else:
    #             print(" \t", end="")
    #         j += 1
    #     print()