def find_missing_number(A):
    n = len(A) + 1
    total_sum = n * (n - 1) // 2
    array_sum = sum(A)
    return total_sum - array_sum


def main():
    A = [0, 1, 2, 4, 5, 6]
    missing_number = find_missing_number(A)
    print(f"The missing number is: {missing_number}")


if __name__ == "__main__":
    main()
