n =5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # Print numbers on the first row, last column, or diagonal
        if i == 1 or j == n or i == j:
            print(j, end=" ")
      
    print()
