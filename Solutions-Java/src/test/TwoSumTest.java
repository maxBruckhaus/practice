import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TwoSumTest {

    @Test
    void twoSumBruteTest1() {
        int[] input = new int[]{2, 7, 11, 15};
        int target = 9;
        int[] solution = new int[]{0, 1};
        assertArrayEquals(solution, TwoSum.twoSumBrute(input, target));
    }

    @Test
    void twoSumBruteTest2() {
        int[] input = new int[]{3, 2, 4};
        int target = 6;
        int[] solution = new int[]{1, 2};
        assertArrayEquals(solution, TwoSum.twoSumBrute(input, target));
    }

    @Test
    void twoSumBruteTest3() {
        int[] input = new int[]{3, 3};
        int target = 6;
        int[] solution = new int[]{0, 1};
        assertArrayEquals(solution, TwoSum.twoSumBrute(input, target));
    }

    @Test
    void twoSumHashTest1() {
        int[] input = new int[]{2, 7, 11, 15};
        int target = 9;
        int[] solution = new int[]{0, 1};
        assertArrayEquals(solution, TwoSum.twoSumHash(input, target));
    }

    @Test
    void TwoSumHashTest2() {
        int[] input = new int[]{3, 2, 4};
        int target = 6;
        int[] solution = new int[]{1, 2};
        assertArrayEquals(solution, TwoSum.twoSumHash(input, target));
    }

    @Test
    void TwoSumHashTest3() {
        int[] input = new int[]{3, 3};
        int target = 6;
        int[] solution = new int[]{0, 1};
        assertArrayEquals(solution, TwoSum.twoSumHash(input, target));
    }
}