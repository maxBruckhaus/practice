public class LongPalSub {

    public static void main(String[] args) {
        String s1 = "babd";
        String s2 = "wowzazazpie";
        String s3 = "abcdefoooooof";
        System.out.println(longPalSubBrute(s1));
        System.out.println(longPalSubBrute(s2));
        System.out.println(longPalSubBrute(s3));
        System.out.println(longPalSubCenter(s1));
        System.out.println(longPalSubCenter(s2));
        System.out.println(longPalSubCenter(s3));
    }

    // Time: O(n^2)
    // Space: O(1)
    public static String longPalSubCenter(String s) {
        if (s.length() < 1) {
            return "";
        } else if (s.length() == 1) {
            return "" + s;
        }

        int start = 0;
        int end = 0;
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);             // center is a character
            int len2 = expandAroundCenter(s, i, i+1);     // center is between 2 characters
            int len = Math.max(len1, len2);
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }

        return s.substring(start, end + 1);
    }

    public static int expandAroundCenter(String s, int left, int right) {
        int L = left, R = right;
        while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
            L--;
            R++;
        }
        return R - L - 1;
    }

    // Time: O(n^3)
    // Space: O(1)
    public static String longPalSubBrute(String s) {
        int longestPal = 0;
        String result = "";

        for (int i = 0; i < s.length() - 1; i++) {
            for (int j = i+1; j < s.length(); j++) {
                String curr = s.substring(i, j+1);
                if (isPalindrome(curr)) {
                    if (curr.length() > longestPal) {
                        longestPal = curr.length();
                        result = curr;
                    }
                }
            }
        }

        if (longestPal == 0){
            return "" + s.charAt(0);
        }

        return result;
    }

    public static boolean isPalindrome(String s) {
        String reverse = "";
        for (int i = s.length()-1; i >= 0; i--) {
            reverse = reverse + s.charAt(i);
        }
        return reverse.equals(s);
    }
}
