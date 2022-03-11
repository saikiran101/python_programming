from collections import deque
class Node:
    def __init__ (self,key):
        self.data=key
        self.left=None
        self.right=None

def printlvlorder(root):
        if root == None:
            return

        queue=deque([])
        queue.append(root)

        while queue:
            print(queue[0].data)
            node=queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)
print("levels")
res=printlvlorder(root)
print(res)

