import java.util.Arrays;

public class FindNonSumInteger {
    public static void findNonSumInteger(int[] A) {
        if (A.length < 2) {
            return;
        }

        int maxElement = Integer.MIN_VALUE;
        for (int num : A) {
            if (num > maxElement) {
                maxElement = num;
            }
        }

        System.out.println(2 * maxElement + 1);
    }

    public static void main(String[] args) {
        int[] array1 = {};
        findNonSumInteger(array1);

        int[] array2 = { 0 };
        findNonSumInteger(array2);

        int[] array3 = { 0, 1, 2, 4, 5, 6 };
        findNonSumInteger(array3);
    }
}
