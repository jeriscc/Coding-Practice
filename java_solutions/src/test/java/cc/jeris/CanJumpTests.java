package cc.jeris;

import org.junit.Test;

import static org.junit.Assert.*;
import cc.jeris.can_jump_two.*;

/**
 * Unit test for simple App.
 */
public class CanJumpTests {
    /**
     * Rigorous Test.
     */
    @Test
    public void testApp() {
        SlowBFSSolution s = new SlowBFSSolution();
        int[] nums = {2,3,1,1,4};
        assertTrue(s.jump(nums) == 2);
    }
}
