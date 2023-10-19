from collections import Counter

def frequency_sort(arr):
    # Use Counter to count the frequency of each element
    counts = Counter(arr)

    # Sort the elements based on frequency, with ties broken by value
    sorted_arr = sorted(arr, key=lambda x: (-counts[x], x))

    return sorted_arr

# Test case
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = frequency_sort(arr)
print("Sorted array by frequency:", sorted_arr)
