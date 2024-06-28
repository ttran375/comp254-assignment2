def find_missing_number(arr):
    """
    Finds the missing number in an array containing n-1 unique integers in the range [0, n-1].
    """
    # Calculate the expected number of elements in the array
    n = len(arr) + 1

    # Find the missing number
    return (n * (n - 1) // 2) - sum(arr)
