Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


Example 1:

Input: 0->1 1->2 2->3 3->3


Output: 1
Explanation: 3 -> 3 is a cycle

Example 2:

Input: 0->1 1->2


Output: 0
Explanation: no cycle in the graph

Your task:
You don’t need to read input or print anything. Your task is to complete the function isCyclic() which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the given directed graph contains a cycle or not.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)


Constraints:
1 ≤ V, E ≤ 10^5