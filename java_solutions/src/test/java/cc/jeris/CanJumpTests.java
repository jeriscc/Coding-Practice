package cc.jeris;

import org.junit.Test;

import static org.junit.Assert.*;
import cc.jeris.can_jump_two.*;

/**
 * Unit test for simple App.
 */
public class CanJumpTests {

    @Test
    public void basicTest() {
        SlowBFSSolution s = new SlowBFSSolution();
        int[] nums = { 2, 3, 1, 1, 4 };
        assertTrue("Slow BFS should work", s.jump(nums) == 2);

        BFSSolution b = new BFSSolution();
        assertTrue("BFS should work", b.jump(nums) == 2);

        GreedySolution g = new GreedySolution();
        assertTrue("Greedy should work", g.jump(nums) == 2);
    }

    /**
     * Tests where the end is unreachable.
     */
    @Test
    public void testImpossible() {
        int[] nums = { 2, 0, 0, 1, 4 };
        SlowBFSSolution s = new SlowBFSSolution();
        assertTrue("Slow BFS should work", s.jump(nums) == -1);

        BFSSolution b = new BFSSolution();
        assertTrue("BFS should work", b.jump(nums) == -1);

        GreedySolution g = new GreedySolution();
        assertTrue("Greedy should work", g.jump(nums) == -1);
    }

    /**
     * Tests solutions against a very large array. Not testing on the slow solution
     * because it will be too slow.
     */
    @Test
    public void testLong() {
        int largeSize = 10000;
        int[] nums = new int[largeSize];
        /**
         * Fill the first n - 2 values with n - 2 to 1. None of them will reach the end.
         */
        for (int i = 0; i < largeSize - 2; i++) {
            nums[i] = largeSize - 2 - i;
        }
        /**
         * Make the second to last element (reachable by all of the previous n-2
         * elements) able to reach the end.
         */
        nums[largeSize - 2] = 1;

        BFSSolution b = new BFSSolution();
        assertTrue("BFS should work", b.jump(nums) == 2);

        GreedySolution g = new GreedySolution();
        assertTrue("Greedy should work", g.jump(nums) == 2);
    }
}
