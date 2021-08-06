from collections import deque
class Solution:
    def widthOfBinaryTree(self, root):
        curr=ans=left=0
        q=deque()
        q.append((root,0,0))
        while q:
            node,pos,depth=q.popleft()
            if node.left:
                q.append((node.left,pos*2,depth+1))
            if node.right:
                q.append((node.right,pos*2 +1,depth +1))
            if curr !=depth:
                left=pos
                curr=depth
            ans=max(pos-left +1,ans)
        return ans
            