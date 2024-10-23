def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        if not swapped:  # If no two elements were swapped, the array is sorted
            break

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Main block for testing the sorting algorithms
if __name__ == "__main__":
    # Bubble Sort
    arr_bubble = [64, 34, 25, 12, 22, 11, 90]
    print("Bubble Sort Example:")
    print("Original array:", arr_bubble)
    bubble_sort(arr_bubble)
    print("Sorted array:", arr_bubble)

    # Merge Sort
    arr_merge = [38, 27, 43, 3, 9, 82, 10]
    print("\nMerge Sort Example:")
    print("Original array:", arr_merge)
    merge_sort(arr_merge)
    print("Sorted array:", arr_merge)

    # Quick Sort
    arr_quick = [10, 7, 8, 9, 1, 5]
    print("\nQuick Sort Example:")
    print("Original array:", arr_quick)
    sorted_quick = quick_sort(arr_quick)
    print("Sorted array:", sorted_quick)
