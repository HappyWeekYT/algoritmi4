# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.results = []
        self.traverse(root)
        self.results = sorted(self.results)
        prev = None
        min_distance = sys.maxsize
        for val in self.results:
            if prev != None:
                min_distance = min(min_distance, val - prev)
            prev = val

        return min_distance
    
    
    def traverse(self, root):
        if not root:
            return
        
        self.results.append(root.val)        
        self.traverse(root.left)
        self.traverse(root.right)