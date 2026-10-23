list1 = list(input("Enter a series of elements separated by space for the first list\n>").split())
list2 = list(input("Enter a series of elements separated by space for the second list\n>").split())

# def find_common_elements(list1: list, list2: list) -> list:
#     list1set = set(list1)
#     list2set = set(list2)

#     common = list1set & list2set

#     result = list(common)
#     output = []
#     for res in result:
#         if res.isdigit():
#             res = int(res)
#         output.append(res)
        

#     #output.sort()

#     return output

def find_common_elements(list1: list, list2: list) -> list:
    list1pointer = 0
    list2pointer = 0
    common = []

    for list1pointer in range(len(list1)):
        for list2pointer in range(len(list2)):
            if list1[list1pointer] == list2[list2pointer]:
                common.append(list1[list1pointer])
                list2pointer += 1
        list1pointer += 1

    return common

print(find_common_elements(list1, list2))