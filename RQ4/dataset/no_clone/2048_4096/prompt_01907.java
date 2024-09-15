/**
 * reference: https://discuss.leetcode.com/topic/28308/java-ac-solution-using-bfs
 */


public String alienOrder(String[] words) 
{
    Map<Character, Set<Character>> graph = new HashMap<>();
    int[] indegree = new int[26];
    buildGraph(graph, words, indegree);
    return bfs(graph, indegree);
}   