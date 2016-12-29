# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def doit(root):
            if root:
                data.append(str(root.val))
                doit(root.left)
                doit(root.right)
            else:   
                data.append('#')
                
        data = []
        doit(root)
        return ' '.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def doit():
            val = next(d)
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = doit()
                node.right = doit()
            return node
            
        d = iter(data.split(' '))
        return doit()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
