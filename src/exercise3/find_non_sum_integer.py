def find_non_sum_integer(A):
    return (
        # If there are at least two elements, calculate the non-sum integer
        2 * max(A) + 1 if len(A) >= 2
        
        # Otherwise, return None
        else None
    )
