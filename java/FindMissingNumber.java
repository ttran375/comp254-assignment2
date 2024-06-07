public class FindMissingNumber {
    public static void findMissingNumber(int[] A) {
        int n = A.length + 1;
        int totalSum = n * (n - 1) / 2;
        int arraySum = 0;

        for (int num : A) {
            arraySum += num;
        }

        System.out.println(totalSum - arraySum);
    }

    public static void main(String[] args) {
        int[] array1 = {};
        findMissingNumber(array1);

        int[] array2 = { 0 };
        findMissingNumber(array2);

        int[] array3 = { 0, 1, 2, 4, 5, 6 };
        findMissingNumber(array3);
    }
}
