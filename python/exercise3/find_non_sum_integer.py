def find_non_sum_integer(A):
    if len(A) < 2:
        return None
    max_element = max(A)
    print(2 * max_element + 1)


def main():
    list1 = []
    find_non_sum_integer(list1)

    list2 = [0]
    find_non_sum_integer(list2)

    list3 = [0, 3, 1, 4, 12, 5, 2]
    find_non_sum_integer(list3)


if __name__ == "__main__":
    main()
