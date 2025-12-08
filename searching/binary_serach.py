

# [2,3,4,5,6]


def binary_search(lst,target):
    size = len(lst)
    start = 0 
    end = size - 1
    print("===========")
    while(start <= end):
        mid = (start + end ) // 2  

        print(mid)
        if lst[mid] == target:
            return mid
        
        elif lst[mid] > target:
            print("====", lst[mid])
            end = mid - 1
        
        elif lst[mid] < target:
            print(";;;", lst[mid])
            start = mid + 1 

    return -1 
    

print(binary_search([2,3,4,5,6,7], 7))