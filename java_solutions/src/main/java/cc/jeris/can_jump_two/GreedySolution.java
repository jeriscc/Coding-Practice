package cc.jeris.can_jump_two;

/**
 * GreedySolution
 * 
 * Reference:
 * https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy
 * 
 * Implicitly a BFS Solution too
 */
public class GreedySolution {

    public int jump(int[] nums) {
        int result = 0, lastJump = 0, furthest = 0;
        int dest = nums.length - 1;
        /**
         * We never check the last element because it's doesn't matter. Also checking
         * the last element might introduce error in cases when the furthest lastJump
         * equals the end.
         */
        for (int i = 0; i < dest; i++) {
            furthest = Math.max(furthest, nums[i] + i);
            if (i == lastJump) {
                result++;
                lastJump = furthest;

                if (lastJump >= nums.length - 1) {
                    return result;
                }
            }
        }
        return dest == 0 ? 0 : -1;
    }
}