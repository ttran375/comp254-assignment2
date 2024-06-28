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
        A[j] = sum(S[0: j + 1]) / (j + 1)
    return A


def main():
    """
    Performs an experimental analysis and visualize the running times.
    """
    # Define different input sizes to test
    input_sizes = [
        100,
        200,
        400,
        800,
        1600,
        3200,
        6400,
    ]

    # Define lists to store execution times
    times1 = []
    times2 = []

    for size in input_sizes:
        # Generate a random list of the given size
        S = np.random.rand(size).tolist()

        # Measure execution time for prefix_average1
        start_time = time.time()
        prefix_average1(S)
        end_time = time.time()
        times1.append(end_time - start_time)

        # Measure execution time for prefix_average2
        start_time = time.time()
        prefix_average2(S)
        end_time = time.time()
        times2.append(end_time - start_time)

    # Plot the execution times on a log-log graph
    plt.figure(figsize=(10, 6))

    # Plot times1 and times2 with log-log scale
    plt.loglog(input_sizes, times1, label="prefix_average1", marker="o")
    plt.loglog(input_sizes, times2, label="prefix_average2", marker="o")

    # Label the axis
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")

    # Add a title to the graph
    plt.title("Execution Time vs Input Size for Prefix Average Algorithms")

    # Add a legend to the graph
    plt.legend()

    # Add a grid to the graph
    plt.grid(True)

    # Save the graph as a PNG file
    plt.savefig("log_log_execution_time_plot.png")


if __name__ == "__main__":
    main()
