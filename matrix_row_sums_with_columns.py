input_matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
for i, numbers in enumerate(input_matrix):
    row_total = 0
    for num in numbers:
        row_total += num
                   
    row_average = row_total/len(numbers)

    print(f"Row{i+1} total: {row_total}| Row{i+1} average: {row_average}")

column_length = len(input_matrix[0])
row_length = len(input_matrix)
column_sum = []
for col in range(column_length):
    total_col = 0
    for row in range(row_length):
        total_col += input_matrix[row][col]
    column_sum.append(total_col)
    print(f"Column{col+1} total: {column_sum[col]}")