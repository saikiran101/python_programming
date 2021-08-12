 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums):
        stack=[]
        for i in nums:
            x=TreeNode(i)
            while stack and stack[-1].value< x:
                x.left=stack.pop()
            if stack:
                stack[-1].right=x
            stack.append(x)
        return stack[0]

