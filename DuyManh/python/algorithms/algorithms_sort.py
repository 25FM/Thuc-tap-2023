def input_Array():
    n = int(input("Nhập số lượng phần tử trong mảng: "))
    arr = []
    for i in range(n):
        value = int(input("Nhập phần tử thứ {}: ".format(i + 1)))
        arr.append(value)
    return arr

def output_Array(arr):
    print(str(arr))  

arr_test = [1, 7, 4, 1, 10, 9, -2]


def output_Array(arr):
    print(str(arr))


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # compare two element continuous
            if arr[j] > arr[j + 1]:
                # swap value two element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # all element small than pivot
        left = [x for x in arr[1:] if x < pivot]
        # all element big than pivot
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


def insertionsort(arr):
    if (n := len(arr)) <= 1:
        return
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while (j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j = j - 1
        # return value to element index i in the loop
        arr[j+1] = key
    return arr


def mergesort(arr):
    if (len(arr) <= 1):
        return arr
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    mergesort(left)
    mergesort(right)
    # get method megre two array
    arr = merge(left, right)
    return arr


def merge(left, right):
    result = []
    i = 0
    j = 0
    
    #check index left and right array
    while (i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            result.append(left[i])
            i+=1
        else: 
            result.append(right[j])
            j+=1
    #extend element remaining left array
    result.extend(left[i:])
    #extend element remaining right array
    result.extend(right[j:])
    return result


#selection sort
def selectionsort(arr):
    for index in range(len(arr)):
        #get index min in each loop
        min = index
        for j in range(index+1, len(arr)):
            if (arr[index] > arr[j]):
                #swap value 2 element
                arr[index],arr[j] = arr[j],arr[index]
    return arr

arr = input_Array()
arr = quicksort(arr)
output_Array(arr)
    
