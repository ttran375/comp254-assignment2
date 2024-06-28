def find_non_sum_integer(A):
    """
    Finds a non-sum integer from the given list A.
    """
    return (
        # If there are at least two elements, calculate the non-sum integer
        2 * max(A) + 1
        if len(A) >= 2
        # Otherwise, return None
        else None
    )
