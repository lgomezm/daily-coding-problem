package problem03;

import org.junit.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class Problem03Test {

    @Test
    public void testDeserialize() {
        String serialized = Problem03.serialize(new Node(
                "root",
                new Node("left",
                        new Node("left.left", null, null), null),
                new Node("right", null, null)));
        assertThat(serialized).isEqualTo(Problem03.serialize(Problem03.deserialize(serialized)));
    }
}
