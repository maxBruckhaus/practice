import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {

    public static void main(String[] args) {
        System.out.println("Hello! Java!");

        // Setting up input
        int[] nums1 = {2, 7, 11, 15};
        int target1 = 9;

        int[] nums2 = {3, 2, 4};
        int target2 = 6;

        int[] nums3 = {3, 3};
        int target3 = 6;

        System.out.println("Brute force approach...");
        int[] result;
        result = twoSumBrute(nums1, target1);
        myPrint(nums1, target1, result);

        result = twoSumBrute(nums2, target2);
        myPrint(nums2, target2, result);

        result = twoSumBrute(nums3, target3);
        myPrint(nums3, target3, result);

        System.out.println("Hash map approach...");
        result = twoSumHash(nums1, target1);
        myPrint(nums1, target1, result);

        result = twoSumHash(nums2, target2);
        myPrint(nums2, target2, result);

        result = twoSumHash(nums3, target3);
        myPrint(nums3, target3, result);
    }

    // Time: O(n^2)
    // Space: O(1)
    public static int[] twoSumBrute(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }

        return new int[] {-1};
    }

    // Time: O(n)
    // Space: O(n)
    public static int[] twoSumHash(int[] nums, int target) {
        Map<Integer, Integer> numsMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            numsMap.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numsMap.containsKey(complement) && numsMap.get(complement) != i) {
                return new int[] {i, numsMap.get(complement)};
            }
        }

        return new int[] {-1};
    }

    public static void myPrint(int[] nums, int target, int[] result) {
        System.out.println("nums = " + Arrays.toString(nums));
        System.out.println("target = " + target);
        System.out.println("result = " + Arrays.toString(result) + "\n");
    }
}
