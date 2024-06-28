def find_missing_number(arr):
    # Calculate the expected number of elements in the array
    n = len(arr) + 1

    # Find the missing number
    return (n * (n - 1) // 2) - sum(arr)
