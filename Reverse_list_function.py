#By using reverse function print the reverse order of the list.
#reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
def reverse_list(numbers):
    i=0
    while i<len(numbers):
        numbers.reverse()
        i=i+1
    print(numbers)
numbers=["Z","A","A","B","E","M","A","R","D"]
reverse_list(numbers)
