#Using sort function sort the given list.
#numbers = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
def ordered_list(numbers):
    i=0
    while i<len(numbers):
        numbers.sort()
        i=i+1
    print(numbers)
numbers=[6,8,4,3,9,56,0,34,7,15]
ordered_list(numbers)