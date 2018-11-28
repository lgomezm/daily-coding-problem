package problem01;

import org.junit.Test;
import static org.assertj.core.api.Assertions.assertThat;

public class Problem01Test {

    @Test
    public void testKContained() {
        int[] numbers = {10, 15, 3, 7};
        int k = 17;
        assertThat(Problem01.evaluate(numbers, k)).isTrue();
    }

    @Test
    public void testKNotFound() {
        int[] numbers = {10, 15, 3, 7};
        int k = 12;
        assertThat(Problem01.evaluate(numbers, k)).isFalse();
    }
}
