def create_matrix(line, column):
    dynamic_matrix = []
    for i in range(line):
        line = [0] * column
        dynamic_matrix.append(line)
    return dynamic_matrix

def fill_matrix(dynamic_matrix):
    for i in range(len(dynamic_matrix)):
        for j in range(len(dynamic_matrix[i])):
            dynamic_matrix[i][j] = int(input(f"Type the value for position [{i}, {j}]: "))
    
    

def print_matrix(dynamic_matrix):
    for i in range(len(dynamic_matrix)):
        for j in range(len(dynamic_matrix[i])):
            print(f"{dynamic_matrix[i][j]}", end=" ")
        print()

def sum_matrix(dynamic_matrix):
    for i in range(len(dynamic_matrix)):
        for j in range(len(dynamic_matrix[i])):
            dynamic_matrix[i][j] = dynamic_matrix[i][j] + dynamic_matrix[i][j]
    
    print_matrix(dynamic_matrix)

def main():
    lines = int(input("Line of the matrix:"))
    columns = int(input("Column of the matrix:"))
    dynamic_matrix = create_matrix(lines, columns)
    fill_matrix(dynamic_matrix)
    print("\nMatrix result:")
    print_matrix(dynamic_matrix)
    print("\nSum matrix:\n")
    sum_matrix(dynamic_matrix)

if __name__ == "__main__":
    main()

