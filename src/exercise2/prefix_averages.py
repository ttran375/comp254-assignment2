import time

import matplotlib.pyplot as plt
import numpy as np


def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A


def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0 : j + 1]) / (j + 1)
    return A


def main():
    input_sizes = [100, 200, 400, 800, 1600, 3200, 6400]

    times1 = []
    times2 = []

    for size in input_sizes:
        S = np.random.rand(size).tolist()

        start_time = time.time()
        prefix_average1(S)
        end_time = time.time()
        times1.append(end_time - start_time)

        start_time = time.time()
        prefix_average2(S)
        end_time = time.time()
        times2.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.loglog(input_sizes, times1, label="prefix_average1", marker="o")
    plt.loglog(input_sizes, times2, label="prefix_average2", marker="o")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Input Size for Prefix Average Algorithms")
    plt.legend()
    plt.grid(True)
    plt.savefig("log_log_execution_time_plot.png")


if __name__ == "__main__":
    main()
