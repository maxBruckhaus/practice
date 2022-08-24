import java.util.HashMap;
import java.util.Map;

public class LongSubNoRepeating {

    public static void main(String[] args) {
        System.out.println("Longest substring without repeating characters!");

        // Setup input
        String s = "abcabcbb";
        int result = longestSubstring(s);
        myPrint(s, result);

        String s2 = "pwwkew";
        result = longestSubstring(s2);
        myPrint(s2, result);

        String s3 = "bbbbb";
        result = longestSubstring(s3);
        myPrint(s3, result);
    }

    public static int longestSubstring(String s) {
        Map<Character, Integer> charMap;
        int maxSize = 1;
        int currSize;

        if (s.length() < 1) {
            return 0;
        }

        for (int i = 0; i < s.length() - 1; i++) {
            charMap = new HashMap<>();
            charMap.put(s.charAt(i), 1);
            currSize = 1;

            for (int j = i+1; j < s.length(); j++) {
                if (charMap.containsKey(s.charAt(j))) {
                    break;
                } else {
                    charMap.put(s.charAt(j), 1);
                    currSize++;
                }
                if (currSize > maxSize) {
                    maxSize = currSize;
                }
            }
        }

        return maxSize;
    }

    public static void myPrint(String input, int result) {
        System.out.println("input = " + input);
        System.out.println("result = " + result);
    }
}
