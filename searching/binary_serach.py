

# [2,3,4,5,6]

def binary_search(lst, target):
    """
    Iterative binary search.
    Returns the index of `target` in `lst`, or -1 if not found.
    Assumes `lst` is sorted in ascending order.
    
    """
    
    start = 0
    end = len(lst) - 1
    print("===========")
    while start <= end:
        mid = (start + end) // 2

        print("mid:", mid, "start:", start, "end:", end)
        if lst[mid] == target:
            return mid

        # Search left
        elif lst[mid] > target:
            print("====", lst[mid])
            end = mid - 1

        # Search right
        else:
            print(";;;", lst[mid])
            start = mid + 1

    return -1


if __name__ == "__main__":
    print(binary_search([2,3,4,5,6,7], 6))