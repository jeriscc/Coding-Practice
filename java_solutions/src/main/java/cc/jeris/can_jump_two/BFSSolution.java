package cc.jeris.can_jump_two;

/**
 * Reference:
 * https://leetcode.com/problems/jump-game-ii/discuss/18028/O(n)-BFS-solution
 * 
 * Compared to my first slow solution, it elminates upfront the looping through
 * visited positions in the array. Time complexity O(n)
 * 
 */

public class BFSSolution {

    public int jump(int[] nums) {
        if (nums.length == 1) {
            return 0;
        } else if (nums[0] > nums.length) {
            return 1;
        }
        int result = 0;
        int i = 0;
        int currentMax = 0;
        int nextMax = 0;
        int dest = nums.length - 1;
        // While i has not exceeded currentMax from the for loop belwo
        while (currentMax - i + 1 > 0) {
            result++;
            for (; i <= currentMax; i++) {
                nextMax = Math.max(nextMax, nums[i] + i);
                if (nextMax >= dest)
                    return result;
            }
            currentMax = nextMax;
        }
        return -1;
    }
}