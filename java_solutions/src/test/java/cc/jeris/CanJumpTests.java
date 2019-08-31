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
        int[] nums = {2,3,1,1,4};
        assertTrue("Slow BFS should work", s.jump(nums) == 2);

        BFSSolution b = new BFSSolution();
        assertTrue("BFS should work", b.jump(nums) == 2);

        GreedySolution g = new GreedySolution();
        assertTrue("Greedy should work", g.jump(nums) == 2);
    }

    @Test
    public void testImpossible() {
        SlowBFSSolution s = new SlowBFSSolution();
        int[] nums = {2,0,0,1,4};
        assertTrue("Slow BFS should work", s.jump(nums) == -1);

        BFSSolution b = new BFSSolution();
        assertTrue("BFS should work", b.jump(nums) == -1);

        GreedySolution g = new GreedySolution();
        assertTrue("Greedy should work", g.jump(nums) == -1);
    }
}
