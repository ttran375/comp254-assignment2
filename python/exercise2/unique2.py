import time
import numpy as np
import pytest


def unique2(S):
    temp = sorted(S)
    for j in range(1, len(temp)):
        if S[j - 1] == S[j]:
            return False
    return True


def measure_execution_time(input_size):
    S = list(range(input_size))
    start_time = time.time()
    unique2(S)
    end_time = time.time()
    return end_time - start_time


def find_max_input_size_within_time_limit(time_limit=60):
    n = 1
    while True:
        execution_time = measure_execution_time(n)
        if execution_time > time_limit:
            break
        n *= 2

    low, high = n // 2, n
    while low < high:
        mid = (low + high) // 2
        execution_time = measure_execution_time(mid)
        if execution_time <= time_limit:
            low = mid + 1
        else:
            high = mid

    return low - 1


time_limit = 1  # 1 second time limit for all cases
max_input_size = find_max_input_size_within_time_limit(time_limit)
within_time_limit_cases = [(time_limit, max_input_size - i) for i in range(25)]
exceed_time_limit_cases = [(time_limit, max_input_size + i + 1) for i in range(25)]
test_cases = within_time_limit_cases + exceed_time_limit_cases


@pytest.mark.parametrize("time_limit, input_size", test_cases)
def test_execution_time(time_limit, input_size):
    execution_time = measure_execution_time(input_size)
    if input_size <= max_input_size:
        assert (
            execution_time <= time_limit
        ), f"Input size {input_size} should run within the time limit {time_limit}"
    else:
        assert (
            execution_time > time_limit
        ), f"Input size {input_size} should exceed the time limit {time_limit}"


if __name__ == "__main__":
    pytest.main()
