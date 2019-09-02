# Course Pre-requisites

Source: Daily Interview Pro

### Problem Statement

You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.

### Thoughts

This seems to be a graph problem. The keys of the hashmap are nodes, while the values are directed edges. We want to verify that the course requisites hashmap and contains no cycles nor has any edges pointing to non-exiting nodes. At the same time, we want to find a way to traverse the graph such that we are always moving upwards (if we define the edge from a course to its requisite as downwards) or horizontally in the graph.

My first solution was a memoized algorithm that assigned each node/course a height. This height is the length of the longest path from a pre-requisite-less course to the course itself (always moving opposite the direction of the edges or upwards). Then, I returend the nodes in ascending-height order, guarenteeing an upward or horizontal movement.

I tried doing a BFS or DFS solution. Came to conclusion that the set up of the HashSet does not facilitate this.
