input_list = list(map(int, input("Enter numbers separated by space: ").split()))

smallest = input_list[0]
Largest = input_list[0]
Total = 0

for num in input_list:
    if num < smallest:
        smallest = num

    if num > Largest:
        Largest = num
    
    Total += num

Average = Total / len(input_list)

print(f"Smallest: {smallest}\nLargest: {Largest}\nTotal: {Total}\nAverage: {Average}")