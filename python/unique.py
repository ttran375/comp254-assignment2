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
    S = list(range(input_size))
    start_time = time.time()
    function(S)
    end_time = time.time()
    return end_time - start_time


def find_max_input_size_within_time_limit(function, time_limit=60):
    n = 1
    while True:
        execution_time = measure_execution_time(function, n)
        if execution_time > time_limit:
            return n // 2
        n *= 2


def main():
    max_n_unique1 = find_max_input_size_within_time_limit(unique1, 1)
    print(
        f"For the brute-force algorithm, the largest value of n within one minute: {max_n_unique1}"
    )

    max_n_unique2 = find_max_input_size_within_time_limit(unique2, 1)
    print(
        f"For the sorted algorithm, the largest value of n within one minute: {max_n_unique2}"
    )


if __name__ == "__main__":
    main()
