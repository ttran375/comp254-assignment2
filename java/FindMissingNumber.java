public class FindMissingNumber {
    public static int findMissingNumber(int[] A) {
        int n = A.length + 1;
        int totalSum = n * (n - 1) / 2;
        int arraySum = 0;

        for (int num : A) {
            arraySum += num;
        }

        return totalSum - arraySum;
    }

    public static void main(String[] args) {
        int[] A = { 0, 1, 2, 4, 5, 6 };
        int missingNumber = findMissingNumber(A);
        System.out.println("The missing number is: " + missingNumber);
    }
}
