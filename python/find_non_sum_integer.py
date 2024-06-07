def find_non_sum_integer(A):
    if len(A) < 2:
        return None
    max_element = max(A)
    return 2 * max_element + 1


def main():
    A = []
    print(find_non_sum_integer(A))

    A = [0]
    print(find_non_sum_integer(A))

    A = [0, 3, 1, 4, 12, 5, 2]
    print(find_non_sum_integer(A))


if __name__ == "__main__":
    main()
