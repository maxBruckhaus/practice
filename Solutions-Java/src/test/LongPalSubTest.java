import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class LongPalSubTest {

    @Test
    void longPalSubBruteTest1() {
        String str = "babd";
        String solution = "bab";
        String result = LongPalSub.longPalSubBrute(str);
        assertEquals(solution, result);
    }

    @Test
    void longPalSubBruteTest2() {
        String str = "wowzazazpie";
        String solution = "zazaz";
        String result = LongPalSub.longPalSubBrute(str);
        assertEquals(solution, result);
    }

    @Test
    void longPalSubBruteTest3() {
        String str = "abcdefoooooof";
        String solution = "foooooof";
        String result = LongPalSub.longPalSubBrute(str);
        assertEquals(solution, result);
    }

    @Test
    void longPalSubCenterTest1() {
        String str = "babd";
        String solution = "bab";
        String result = LongPalSub.longPalSubCenter(str);
        assertEquals(solution, result);
    }

    @Test
    void longPalSubCenterTest2() {
        String str = "wowzazazpie";
        String solution = "zazaz";
        String result = LongPalSub.longPalSubCenter(str);
        assertEquals(solution, result);
    }

    @Test
    void longPalSubCenterTest3() {
        String str = "abcdefoooooof";
        String solution = "foooooof";
        String result = LongPalSub.longPalSubCenter(str);
        assertEquals(solution, result);
    }
}