def find_non_sum_integer(A):
    n = len(A)
    if n == 0:
        return 0
    
    max_element = max(A)
    return 2 * max_element + 1


def main():
    A = [0, 3, 1, 4, 12, 5, 2]
    non_sum_integer = find_non_sum_integer(A)
    print(
        f"An integer that cannot be formed as the sum of two integers in the array is: {non_sum_integer}"
    )


if __name__ == "__main__":
    main()
