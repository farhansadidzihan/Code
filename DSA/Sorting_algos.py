# || =====\\ Bubble Sort is Sorting Algorithm //===== ||

# || 01 ||
def bubble_sort(list):
    n = len(list)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                print(list, "--> ", end = "")

if __name__ == "__main__":
    unsorted_list = [30, 10, 25, 15, 70]
    bubble_sort(unsorted_list)
    print(unsorted_list)


# || =====\\ Insertion Sort is Sorting Algorithm //===== ||

# || 01 ||
def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        item = list[i]
        j = i - 1
        while j >= 0 and list[j] > item:
            list[j + 1] = list[j]
            j = j - 1
            list[j + 1] = item
            print(list, "--> ", end = "")

if __name__ == "__main__":
    unsorted_list = [30, 10, 25, 15, 70]
    insertion_sort(unsorted_list)
    print(unsorted_list)

# || =====\\ Selection Sort is Sorting Algorithm //===== ||

# || 01 ||
def selection_sort(list):
    n = len(list)
    for i in range(0, n - 1):
        index_min = i
        for j in range(i + 1, n):
            if list[j] < list[index_min]:
                index_min = j
        if index_min != i:
            list[i], list[index_min] = list[index_min], list[i]
            print(list, "--> ", end = "")

if __name__ == "__main__":
    unsorted_list = [30, 10, 25, 15, 70]
    selection_sort(unsorted_list)
    print(unsorted_list)

# || =====\\ Merge Sort is one of the Most Popular Sorting Algorithm //===== ||

# || In Merge Sort, At First We divide the list into two sub-list then, We sort them differently and After sorting both sub-lists, We merge the sub-lists || This typical algorithms are called "Divide and Conquer" ||
# || The Time Complexity of Dividing part is O(log n) & Merging part is O(n) || So, The Time Complexity of the whole Algorithm is O(n log n) ||

# || 01 ||
def split(list):
    mid = len(list) // 2
    left = list[ : mid]
    right = list[mid : ]
    return left, right

def merge(left_list, right_list):
    li = []
    i, j = 0, 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            li.append(left_list[i])
            i += 1
        else:
            li.append(right_list[j])
            j += 1
    while i < len(left_list):
        li.append(left_list[i])
        i += 1
    while j < len(right_list):
        li.append(right_list[j])
        j += 1
    return li

def merge_sort(list):
    ''' Sorts a list in order & returns a new sorted list '''
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)

if __name__ == "__main__":
    unsorted_list = [30, 10, 25, 15, 70]
    merge_sort(unsorted_list)
    print(unsorted_list)

# || =====\\ Quick Sort is one of the Most Popular Sorting Algorithms //===== ||

# || In Quick Sort, At First We select a number from the list, that's called "Pivot". Put the Pivot and put all lesser nubers in left & greater numbers in right side of the Pivot . This is called "Partison"||
# || This is "Divide and Conquer" type Algorithm || The Time Complexity of the Partison is O(n) & Diving is O(log n) || So, The Time Complexity of the whole Algorithm is O(n log n), but worst case it takes O(n^2) ||

# || 01 ||
def quick_sort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1 : ]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    # print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot)) # With Debug Output 
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

if __name__ == "__main__":
    unsorted_list = [30, 10, 25, 15, 70]
    quick_sort(unsorted_list)
    print(unsorted_list)
