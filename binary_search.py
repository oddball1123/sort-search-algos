# Returns index of x in arr if present, else -1
def binary_search(arr, l, r, target):
    """
    Module to implement binary search

    :param arr: integer sorted list
    :param l: leftmost index of list for binary search
    :param r: rightmost index of list for binary search
    :param target: integer to search for
    :return: index of target
    """
    while r >= l:
        # calculate middle index of the search array
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, l, mid - 1, target)
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, r, target)
    return -1


if __name__ == "__main__":
    # Test array
    int_arr = list(map(int, input().split(' ')))
    n = len(int_arr)
    target = int(input())

    # Function call
    result = binary_search(int_arr, 0, len(int_arr) - 1, target)

    if result != -1:
        print("Element is present at index ", result)
    else:
        print("Element is not present in array")
