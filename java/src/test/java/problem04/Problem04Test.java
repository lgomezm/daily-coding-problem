package problem04;

import org.junit.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class Problem04Test {

    @Test
    public void testMinInRange() {
        int[] numbers = { 4, 3, -1, 1};
        assertThat(Problem04.findSmallestNotContained(numbers)).isEqualTo(2);
    }

    @Test
    public void testMinOutOfRange() {
        int[] numbers = { 2, 1, 0};
        assertThat(Problem04.findSmallestNotContained(numbers)).isEqualTo(3);
    }
}
