package cc.jeris.can_jump_two;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

/**
 * My first try with solving this problem. It is too slow because it checks
 * every posible increment from each position. Bad time complexity.
 */
public class SlowBFSSolution {
    private Queue<Integer> q;
    private HashSet<Integer> h;

    public int jump(int[] nums) {
        if (nums.length == 1) {
            return 0;
        } else if (nums[0] > nums.length) {
            return 1;
        }
        q = new LinkedList<>();
        h = new HashSet<Integer>();
        addMoves(nums, 0);

        int result = 0;
        int dest = nums.length - 1;
        while (!q.isEmpty()) {
            result++;
            int size = q.size();

            for (int i = 0; i < size; i++) {
                int pos = q.poll();
                if (pos >= dest) {
                    return result;
                }
                addMoves(nums, pos);
            }
        }
        return -1;
    }

    private void addMoves(int[] nums, int pos) {
        for (int i = nums[pos]; i >= 1; i--) {
            if (!h.contains(pos + i)) {
                q.add(pos + i);
                h.add(pos + i);
            }
        }
    }
}