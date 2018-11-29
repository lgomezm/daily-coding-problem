package problem04;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * This problem was asked by Stripe.
 *
 * Given an array of integers, find the first missing positive integer in linear time
 * and constant space. In other words, find the lowest positive integer that does not
 * exist in the array. The array can contain duplicates and negative numbers as well.
 *
 * For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
 *
 * You can modify the input array in-place.
 */
public class Problem04 {

    static int findSmallestNotContained(int[] array) {
        Set<Integer> set = new HashSet<>();
        int max = 0;
        for (int n : array) {
            if (n > 0) {
                set.add(n);
                if (n > max) {
                    max = n;
                }
            }
        }
        for (int i = 1; i <= max; i++) {
            if (!set.contains(i)) {
                return i;
            }
        }
        return max + 1;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String line = in.nextLine();
        String[] parts = line.split(" ");
        int[] numbers = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            numbers[i] = Integer.parseInt(parts[i]);
        }
        System.out.println(findSmallestNotContained(numbers));
    }
}
