package problem03;

import java.util.LinkedList;
import java.util.List;

/**
 * This problem was asked by Google.
 *
 * Given the root to a binary tree, implement serialize(root),
 * which serializes the tree into a string, and deserialize(s),
 * which deserializes the string back into the tree.
 *
 * For example, given the following Node class
 *
 * class Node:
 *     def __init__(self, val, left=None, right=None):
 *         self.val = val
 *         self.left = left
 *         self.right = right
 * The following test should pass:
 *
 * node = Node('root', Node('left', Node('left.left')), Node('right'))
 * assert deserialize(serialize(node)).left.left.val == 'left.left'
 */
class Problem03 {

    static String serialize(Node node) {
        if (node == null) {
            return "";
        }
        return "["+node.val+","+serialize(node.left)+","+serialize(node.right)+"]";
    }

    static Node deserialize(String text) {
        return deserialize(text, 1);
    }

    private static Node deserialize(String text, int currLevel) {
        if (text.equals("")) {
            return null;
        } else if (text.charAt(0) != '[' || text.charAt(text.length() - 1) != ']') {
            throw new RuntimeException("Malformed tree");
        }
        int level = currLevel - 1;
        List<String> parts = new LinkedList<>();
        StringBuilder part = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (c == '[') {
                level++;
                if (currLevel != level) {
                    part.append(c);
                }
            } else if (c == ',') {
                if (currLevel == level) {
                    parts.add(part.toString());
                    part = new StringBuilder();
                } else {
                    part.append(c);
                }
            } else if (c == ']') {
                if (currLevel == level) {
                    parts.add(part.toString());
                } else {
                    part.append(c);
                }
                level--;
            } else {
                part.append(c);
            }
        }
        if (parts.size() != 3) {
            throw new RuntimeException("Malformed tree");
        }
        return new Node(parts.get(0), deserialize(parts.get(1), currLevel+1), deserialize(parts.get(2), currLevel+1));
    }
}
