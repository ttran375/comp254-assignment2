import time


def unique1(S):
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if S[j] == S[k]:
                return False
    return True


def unique2(S):
    temp = sorted(S)
    for j in range(1, len(temp)):
        if S[j - 1] == S[j]:
            return False
    return True


def measure_execution_time(function, input_size):
    """
    Measures the execution time of a function given an input size.
    """
    # Generate a list of unique integers of size 'input_size'
    # for consistent maximum execution time measurement
    S = list(range(input_size))

    # Record the start time before the function execution
    start_time = time.time()

    # Execute the function with the generated list
    function(S)

    # Record the end time after the function execution
    end_time = time.time()

    # Calculate and return the execution time
    return end_time - start_time


def find_max_input_size_within_time_limit(function, time_limit=60):
    """
    Finds the maximum input size for which the function's execution time is within the given time.
    """
    n = 1
    # Exponentially increase 'n' to find an upper bound where execution time exceeds 'time_limit'
    while True:
        execution_time = measure_execution_time(function, n)

        # If execution time exceeds the limit, break the loop
        if execution_time > time_limit:
            break
        n *= 2

    # Use binary search for continuous variables to find the maximum 'n' where execution time is
    # within the limit
    low, high = n // 2, n
    while low < high:
        mid = (low + high) // 2

        # Measure execution time for the midpoint 'mid'
        execution_time = measure_execution_time(function, mid)

        # If execution time is within the limit, search the upper half
        if execution_time <= time_limit:
            low = mid + 1
        else:
            # If execution time exceeds the limit, search the lower half
            high = mid

    # Return the largest 'n' where execution time is within the limit
    return low - 1


def main():
    max_n_unique1 = find_max_input_size_within_time_limit(unique1, 1)
    print(
        f"For the brute-force algorithm, the largest value of n within the time: {max_n_unique1}"
    )

    max_n_unique2 = find_max_input_size_within_time_limit(unique2, 1)
    print(
        f"For the sorted algorithm, the largest value of n within the time: {max_n_unique2}"
    )


if __name__ == "__main__":
    main()
