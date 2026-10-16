def two_sums(Target):
    Numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    valid_nums = {}

    for num in Numbers:
        if num <= Target:
            valid_nums[num] = Numbers.index(num)

#Output stored the index of the ttwo numbers that sums up to the target number
    output = []
    for key in valid_nums:
        needed = Target - key
        if needed in valid_nums and needed != key:
            output.append(valid_nums[key])

    return output        
    
print(two_sums(9))