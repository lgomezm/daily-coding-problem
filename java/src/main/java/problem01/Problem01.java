package problem01;

import java.util.HashSet;
import java.util.Set;

/**
 * Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
 *
 * For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
 */
class Problem01 {

    static boolean evaluate(int[] numbers, int k) {
        Set<Integer> visited = new HashSet<>();
        for (int n : numbers) {
            if (visited.contains(k - n)) {
               return true;
            }
            visited.add(n);
        }
        return false;
    }
}
