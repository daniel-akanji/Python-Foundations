input_list = [[2,4,6],[1,3,5],[10,20,30]]

for i, numbers in enumerate(input_list):
    total = 0
    
    for num in numbers:
        total += num 
        
    print(f"Row{i+1} total: {total}")