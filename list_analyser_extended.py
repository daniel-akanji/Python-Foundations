def find_smallest(my_list):
    small = my_list[0]
    small_index = 0
    for i, number in enumerate(my_list):
        if number < small:
            small = number
            small_index = i
            break
    return small, small_index

def find_largest(my_list):
    large = my_list[0]
    large_index = 0
    for i, number in enumerate(my_list):
         if number > large:
            large = number
            large_index = i
            break
    return large, large_index

def total_and_average(my_list):
    total = 0
    for number in my_list:
        total += number
    Average = round(total/len(my_list), 2)
    count = 0
    for number in my_list:
        if number > Average:
            count += 1
    return total, Average, count

def main():
    my_list = list(map(int, input("Enter numbers separated by space: ").split()))
    small, small_index = find_smallest(my_list)
    large, large_index = find_largest(my_list)
    total, Average, count = total_and_average(my_list)

    
    return f"Input List: {my_list}\nSmallest: {small} (at index {small_index})\nLargest: {large} (at index {large_index})\nTotal: {total}\nAverage: {Average}\nNumbers abpve average: {count}"

print(main())    