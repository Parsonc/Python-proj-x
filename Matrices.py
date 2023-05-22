matrix = [] # Create an empty list
numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))
Row=1
Column=1
for row in range(numberOfRows):
    matrix.append([]) # Add an empty new row
    for column in range(numberOfColumns):
        value = eval(input("Enter Row"+str(Row)+" Column"+str(Column)+" interger :"))
        matrix[row].append(value)
        Column=Column+1
    Column=1
    Row=Row+1
print(matrix)
