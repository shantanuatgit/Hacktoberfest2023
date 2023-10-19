def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Find the minimum and maximum values in the input array
    min_val = min(arr)
    max_val = max(arr)

    # Create empty buckets
    num_buckets = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for num in arr:
        index = num - min_val
        buckets[index].append(num)

    # Sort each bucket and concatenate them
    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr

# Test case
arr = [3, 6, 1, 8, 5, 2, 7, 4]
sorted_arr = bucket_sort(arr)
print("Sorted array is:", sorted_arr)
