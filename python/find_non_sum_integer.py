def find_non_sum_integer(A):
    n = len(A)
    if n < 2:
        return 1 if n == 0 else A[0] + 1

    max_elem = max(A)
    element_set = set(A)

    for target in range(2, 2 * max_elem + 1):
        found = False
        for num in A:
            if (target - num) in element_set:
                found = True
                break
        if not found:
            return target


def main():
    A = [0, 3, 1, 4, 12, 5, 2]
    non_sum_integer = find_non_sum_integer(A)
    print(
        f"An integer that cannot be formed as the sum of two integers in the array is: {non_sum_integer}"
    )


if __name__ == "__main__":
    main()
