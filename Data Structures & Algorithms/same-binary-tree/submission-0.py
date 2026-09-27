# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #do bfs and check at each level if there is a left and right child 
        queue = deque()
        queue.append(p)
        queue.append(q)

        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()

            if not node1 and not node2: #if no children, continue
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.left)
            queue.append(node1.right)
            queue.append(node2.right)
        return True