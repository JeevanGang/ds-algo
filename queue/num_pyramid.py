#      0
#     101
#    21012
#   3210123


def pyramid(indent):
    for i in range(0, indent):
        for j in range(1, indent-i+1):
            print(end=" ")
        for j in range(i, 0, -1):
            print(j, end="")
        for j in range(0, i+1):
            print(j, end="")
        print()
    for z in range(0, indent-1):
        for k in range(0, z+2):
            print(end=" ")
        for k in range(indent-z-2, -1, -1):
            print(k, end="")
        for k in range(1, indent-z-1):
            print(k, end="")
        print()


pyramid(6)
