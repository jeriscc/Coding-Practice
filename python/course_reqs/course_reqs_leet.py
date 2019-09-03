from typing import List

class Solution:
    """
    Source: https://leetcode.com/problems/course-schedule-ii/
    We are trying to verify that this is a directed acyclic graph

    Thought for a long time whether we could eliminate creating a graph from the edge list.
    Seems like that is infeasible. Should probably share about my thoughts on eliminating the
    graph and be told that that is not a good idea.

    Took inspiration from top submissions. You want to memorize info about classes that show
    whether they are takeable or visited.
    - One way to memorize is to instantiate a list the size of the number of courses and mark
    them with values. 1 = takeable, -1 = already visited in current traversal, 0 = unvisited
    - Another way is to instatiate two sets. One for visited, and one for visited in current
    traversal. Visited is a superset of current.

    I tried to empircally optimize the leetcode submission time, but it was very inconsistent.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Eliminate a few simple cases using graph theory
        if numCourses * (numCourses - 1) / 2 < len(prerequisites):
            return False
        elif len(prerequisites) == 1:
            return True

        courses = range(numCourses)  # memoize this course list

        # Build the requirements graph from the edge list
        graph = [set() for _ in courses]
        for prereq, course in prerequisites:
            graph[course].add(prereq)

        def is_cyclic(course: int) -> bool:
            if course in visited:
                return course in current
            visited.add(course)
            current.add(course)
            if any(is_cyclic(n) for n in graph[course]):
                return True
            current.remove(course)
            return False

        current = set() # set of courses in current traversal
        visited = set()
        return all(c in visited or not is_cyclic(c) for c in courses)

def test():
    s = Solution()

    assert not s.canFinish(3, [[0,2],[1,2],[2,0]])
    assert s.canFinish(2,[[1,0]])

test()
