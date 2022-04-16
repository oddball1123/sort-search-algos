import math


def jump_search(array, x, n):
    # return if the target is not in the array
    if x < array[0] or x > array[n]:
        return -1

    # get ideal jump size
    jump_size = int(math.sqrt(n + 1))

    # initialize first block
    left_index = 0
    right_index = jump_size + 1

    while right_index >= left_index:
        if array[left_index] <= x <= array[right_index]:
            for i in range(left_index, right_index + 1):
                if array[i] == x:
                    return i

        left_index = right_index + 1
        right_index += jump_size

        # rightmost comparison index cannot be more than max array index
        if right_index > n:
            right_index = n

    return -1


if __name__ == '__main__':

    int_arr = list(map(int, input().split(' ')))
    target = int(input())

    # Function call
    result = jump_search(int_arr, target, len(int_arr) - 1)

    if result != -1:
        print("Element is present at index ", result)
    else:
        print("Element is not present in array")
