def second_largest(): 
    my_list = list(map(int, input("Enter numbers separated by space: ").split())) #Syntax to take in a list as input

    max = my_list[0]

    for number in my_list:
        if number > max:
            max = number

    my_list.remove(max) #list.remove() deletes the item and returns None that's why you will see None if you save it under a variable or try to ptint. None instead of the list. remove() modifies the list in place; it doesn't give you back anything useful to print.
    new_list = my_list
    if max in new_list: #to remove duplicated highest number
        new_list.remove(max)
        
    second = new_list[0]

    for nums in new_list:
        if nums > second:
            second = nums

    print(second)

second_largest()#pyttx3 library