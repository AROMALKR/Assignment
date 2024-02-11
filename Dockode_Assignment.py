def print_hexagon_pattern(rows, columns):
    for i in range(rows):
        if i%2==0:
            print("___", end="")
            print()

        for j in range(columns):
            if i % 2 == 0:
                print("/  \\", end="")
            else:
                print("\\___/", end="")
        print()


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
print_hexagon_pattern(rows, columns)

