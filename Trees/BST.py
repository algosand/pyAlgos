"""
Implementation of binary search tree, not optimized. 
"""
class node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,val):
        self.root=node(val)

    def insert(self,val,target):
        """
        Inserts a node into the BST.
        """
        new_node=node(val)
        cur=self.root
        while cur:
            if abs(val-cur.val)<=target:
                return True
            elif val<cur.val:
                if cur.left:
                    cur=cur.left
                else:
                    cur.left=new_node
                    break
            else:
                if cur.right:
                    cur=cur.right
                else:
                    cur.right=new_node
                    break
        return False

    def delete(self,val):	
        """
        Deletes a node from the BST.
        """
        def dfs(node):
            cur=node
            while cur.left:
                cur=cur.left
            return cur
        cur=parent=self.root
        while cur:
            if cur.val==val:
                if parent is cur:
                    if cur.right:
                        self.root=cur.right
                        dfs(cur.right).left=cur.right.left
                        self.root.left=cur.left
                    else:
                        self.root=cur.left
                elif cur.right:
                    parent.right=cur.right
                    dfs(cur.right).left=cur.left
                else:
                    if parent.right and parent.right.val==val:
                        parent.right=cur.left
                    else:
                        parent.left=cur.left
            parent=cur
            if val<cur.val:
                cur=cur.left
            else:
                cur=cur.right
        return self.root

"""
To be continued:  AVL Tree - self balancing bst
https://medium.com/@aksh0001/avl-trees-in-python-bc3d0aeb9150
"""

