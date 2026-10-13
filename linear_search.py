input_list = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Target: "))
target_index = 0

for i in range(len(input_list)):
    if target == input_list[i]:
        target_index = i
        break

if target in input_list:
    print(f"Found at index {target_index}")
else: 
    print("Target not found")