/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
    // Base Case
    if node == nil{
        return nil
    }

    oldtonew := make(map[*Node]*Node)

    var dfs func(n *Node) *Node

    dfs = func(n *Node) *Node {
        // Check if node in the hashmap or not
        if copyy, found := oldtonew[n]; found{
            return copyy
        }

        // Creating a new node with same value
        copyy := &Node{Val: n.Val}
        // Put into hashmap
        oldtonew[n] = copyy

        for _, nei := range n.Neighbors {
            copyy.Neighbors = append(copyy.Neighbors, dfs(nei))
        }
        return copyy
    }

    return dfs(node)
}
// T.C. -> O(V + E) where V is the vertices that we are visiting each vertices and E is the edges
// S.C. -> O(V) Hash map stores every node
