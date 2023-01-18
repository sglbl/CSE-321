# if sum of array elements is even or odd using divide conquer algorithm in python

def is_even(array):
    if len(array) == 1:
        return array[0]
    count = len(array)

    return ((is_even(array[0:count//2]) + is_even(array[count//2:])) % 2) == 0


array = [1,2,6,4,3,4]
sum = 0
print(is_even(array))
