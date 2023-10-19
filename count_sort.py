def counting_sort(arr):
    if not arr:
        return arr

    # Find the maximum value in the array
    max_value = max(arr)

    # Create a list to store the count of each element
    count = [0] * (max_value + 1)

    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(max_value + 1):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

# Test case
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
