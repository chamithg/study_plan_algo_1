"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        nodes = [[]]

        def treverse(root,level):
            if not root:return
            if level < len(nodes):
                nodes[level].append(root)
            else:
                nodes.append([root])
            treverse(root.left,level+1)
            treverse(root.right, level+1)


        treverse(root,0)
        for i in nodes:
            for j,val in enumerate(i):
                if j < len(i)-1:
                    i[j].next = i[j+1]
                else:
                    i[j].next = None

        return root