import java.util.Arrays;

class Uniqueness {
  public static boolean unique1(int[] data) {
    int n = data.length;
    for (int j = 0; j < n - 1; j++)
      for (int k = j + 1; k < n; k++)
        if (data[j] == data[k])
          return false;
    return true;
  }

  public static boolean unique2(int[] data) {
    int n = data.length;
    int[] temp = Arrays.copyOf(data, n);
    Arrays.sort(temp);
    for (int j = 0; j < n - 1; j++)
      if (temp[j] == temp[j + 1])
        return false;
    return true;
  }

  public static double measureExecutionTime(IntArrayFunction function, int inputSize) {
    int[] S = new int[inputSize];
    for (int i = 0; i < inputSize; i++)
      S[i] = i;
    long startTime = System.nanoTime();
    function.apply(S);
    long endTime = System.nanoTime();
    return (endTime - startTime) / 1e9;
  }

  public static int findMaxInputSizeWithinTimeLimit(IntArrayFunction function, double timeLimit) {
    int n = 1;
    while (true) {
      double executionTime = measureExecutionTime(function, n);
      if (executionTime > timeLimit)
        break;
      n *= 2;
    }

    int low = n / 2;
    int high = n;
    while (low < high) {
      int mid = (low + high) / 2;
      double executionTime = measureExecutionTime(function, mid);
      if (executionTime <= timeLimit) {
        low = mid + 1;
      } else {
        high = mid;
      }
    }
    return low - 1;
  }

  interface IntArrayFunction {
    boolean apply(int[] array);
  }

  public static void main(String[] args) {
    int maxNUnique1 = findMaxInputSizeWithinTimeLimit(Uniqueness::unique1, 0.1);
    System.out.println("For the brute-force algorithm, the largest value of n within one minute: " + maxNUnique1);

    int maxNUnique2 = findMaxInputSizeWithinTimeLimit(Uniqueness::unique2, 0.1);
    System.out.println("For the sorted algorithm, the largest value of n within one minute: " + maxNUnique2);
  }
}
