def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Take input array from user
def take_input():
    n = int(input("Enter the number of elements: "))
    arr = []
    for _ in range(n):
        element = int(input("Enter an element: "))
        arr.append(element)
    return arr

# Example usage:
arr = take_input()
print("Original array is:", arr)

# Sort the array using Selection Sort
selection_sort(arr)
print("Sorted array is:", arr)
