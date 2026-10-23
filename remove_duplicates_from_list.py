nums = list(input("Enter a series of elements separated by space\n>").split())


def remove_duplicate(nums: list) -> list:
    removed = set(nums)
    output = list(removed)
    result = []
    
    for elems in output:
        if elems.isdigit():
            elems = int(elems)

        result.append(elems)

    result.sort()
    return result

print(remove_duplicate(nums))