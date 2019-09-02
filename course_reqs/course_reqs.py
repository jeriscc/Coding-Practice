from typing import List, Dict, Set
Vector = List[str]

#
# Solution seems to be O(n) time and space.
#
class Solution:
    # Keep track of how course levels
    course_levels = {}

    # Keep track of the course requisites graph
    course_map = {}

    def courses_to_take(self, map: Dict[str, Vector]) -> Vector:
        self.course_levels = {}
        self.course_map = map

        for course in map:
            level = self.get_level(course, set(), 0)
            if level == None:
                return None
            self.course_levels[course] = level
        return sorted(self.course_levels.keys(), key=lambda course: self.course_levels[course])

    def get_level(self, course: str, visited: Set[str], cum_level: int) -> int:
        # Return precomputed cources
        if course in self.course_levels:
            return self.course_levels[course]
        # Bail on non-takeable courses
        elif course not in self.course_map:
            return None
        # Base case
        elif self.course_map[course] == []:
            return cum_level + 1
        # If we are in a cycle
        elif course in visited:
            return None

        visited.add(course)
        # Find level of this course
        max = 0
        for req in self.course_map[course]:
            req_level = self.get_level(req, visited, cum_level + 1)
            self.course_levels[req] = req_level
            if req_level == None:
                return None
            if req_level > max:
                max = req_level
        return req_level
