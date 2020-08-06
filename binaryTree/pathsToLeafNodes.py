class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def findLeafs(root):
            if not root:
                return
            dq = [(root, [])]
            path = []
            paths = []
            while dq:
                node, i = dq.pop()
                i.append(node.val)
                print(i)
                if not node.left and not node.right:
                    paths.append(i)
                    print(paths)
                    continue
                if node.left:
                    dq.append((node.left, i))
                if node.right:
                    dq.append((node.right, i))
            print(paths)
            print(path)
            return paths

        findLeafs(root)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    root.left = node1
    root.right = node2
    node1.right = node3
    print(root)
    dist = 3
    sol.countPairs(root, dist)