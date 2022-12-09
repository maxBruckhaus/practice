import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class LongSubNoRepeatingTest {

    @Test
    void longestSubstringTest1(){
        assertEquals(3, LongSubNoRepeating.longestSubstring("abcabcbb"));
    }

    @Test
    void longestSubstringTest2(){
        assertEquals(3, LongSubNoRepeating.longestSubstring("pwwkew"));
    }

    @Test
    void longestSubstringTest3(){
        assertEquals(1, LongSubNoRepeating.longestSubstring("bbbbb"));
    }
}
