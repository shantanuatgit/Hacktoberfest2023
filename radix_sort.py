def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    num_digits = len(str(max_num))

    # Initialize the buckets
    buckets = [[] for _ in range(10)]

    # Start from the least significant digit to the most significant digit
    for digit in range(num_digits):
        # Distribute elements into buckets based on the current digit
        for num in arr:
            index = (num // 10**digit) % 10
            buckets[index].append(num)

        # Concatenate the elements from the buckets
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
            bucket.clear()

    return arr

# Test case
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print("Sorted array:", sorted_arr)
