# Course Pre-requisites

### Problem Statement

You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.

### Thoughts

This seems to be a tree / graph problem. The keys of the hashmap are nodes, while the values are edges. We want to verify that the course requisites diagram is a forrest and contains no cycles nor has any edges pointing to non-exiting nodes. At the same time, we want to find a way to traverse the tree such that we are always moving upwards or horizontally in trees in the forrest, never downwards.

My first solution was a memoized algorithm that determined the how high each node was on their respective trees. Then, I returend the nodes in ascending-height order, guarenteeing an upward or horizontal movement.
