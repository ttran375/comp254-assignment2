def find_missing_number(A):
    n = len(A) + 1
    total_sum = n * (n - 1) // 2
    array_sum = sum(A)
    return total_sum - array_sum


def main():
    list1 = []
    print(find_missing_number(list1))

    list2 = [0]
    print(find_missing_number(list2))

    list3 = [0, 1, 2, 4, 5, 6]
    print(find_missing_number(list3))


if __name__ == "__main__":
    main()
