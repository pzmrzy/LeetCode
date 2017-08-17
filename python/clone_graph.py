# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        root = UndirectedGraphNode(node.label)
        stack = [node]
        visit = {}
        visit[node.label] = root
        while stack:
            now = stack.pop()
            for n in now.neighbors:
                if n.label not in visit:
                    stack.append(n)
                    visit[n.label] = UndirectedGraphNode(n.label)
                visit[now.label].neighbors.append(visit[n.label])
        return root
