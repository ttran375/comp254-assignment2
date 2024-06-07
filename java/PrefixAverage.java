import java.util.Random;

class PrefixAverage {

  public static double[] prefixAverage1(double[] x) {
    int n = x.length;
    double[] a = new double[n];
    for (int j = 0; j < n; j++) {
      double total = 0;
      for (int i = 0; i <= j; i++)
        total += x[i];
      a[j] = total / (j + 1);
    }
    return a;
  }

  public static double[] prefixAverage2(double[] x) {
    int n = x.length;
    double[] a = new double[n];
    double total = 0;
    for (int j = 0; j < n; j++) {
      total += x[j];
      a[j] = total / (j + 1);
    }
    return a;
  }

  public static void main(String[] args) {
    int[] inputSizes = { 100, 200, 400, 800, 1600, 3200, 6400 };

    double[] times1 = new double[inputSizes.length];
    double[] times2 = new double[inputSizes.length];

    Random rand = new Random();

    for (int k = 0; k < inputSizes.length; k++) {
      int size = inputSizes[k];
      double[] S = new double[size];
      for (int i = 0; i < size; i++) {
        S[i] = rand.nextDouble();
      }

      long startTime = System.nanoTime();
      prefixAverage1(S);
      long endTime = System.nanoTime();
      times1[k] = (endTime - startTime) / 1e9;

      startTime = System.nanoTime();
      prefixAverage2(S);
      endTime = System.nanoTime();
      times2[k] = (endTime - startTime) / 1e9;
    }

    for (int i = 0; i < inputSizes.length; i++) {
      System.out.println("Input Size: " + inputSizes[i] +
          ", Time1: " + times1[i] +
          ", Time2: " + times2[i]);
    }
  }
}
