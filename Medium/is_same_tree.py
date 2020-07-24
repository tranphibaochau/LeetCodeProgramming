def isSameTree(self, p, q):
	if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left)  and self.isSameTree(p.right, q.right)