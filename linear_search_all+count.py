def find_target(input_list, target):
    target_indices = []
    count = 0 
    for i in range(len(input_list)):
        if target == input_list[i]:
            target_indices.append(i)
            count += 1
    First = target_indices[0]
    Last = target_indices[len(target_indices)-1]

    return target_indices, count, First, Last
        
def main():
    input_list = list(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Target: "))

    if target in input_list:
        target_indices, count, First, Last = find_target(input_list, target)
        return f"Starting list: values = {input_list}\nTarget: {target} -> Found at indices: {target_indices}|Count: {count}| First: {First}| Last: {Last}"
    else:
        return f"Starting list: values = {input_list}\nTarget: {target} -> Target not found"

print(main())