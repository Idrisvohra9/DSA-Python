"""
BINARY TREE PROBLEMS & SOLUTIONS
===============================
Collection of well-known binary tree problems with optimal solutions.
Binary trees are hierarchical data structures where each node has at most two children.
They form the foundation for many advanced algorithms and data structures.
"""

from collections import deque

class TreeNode:
    """Standard binary tree node definition."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================================================
# PROBLEM 1: BINARY TREE TRAVERSALS
# ============================================================================
def inorder_traversal(root):
    """
    Problem: Traverse binary tree in inorder (left, root, right).
    
    Approach: Recursive and iterative solutions
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height
    """
    result = []
    
    def inorder_recursive(node):
        if node:
            inorder_recursive(node.left)
            result.append(node.val)
            inorder_recursive(node.right)
    
    inorder_recursive(root)
    return result

def inorder_iterative(root):
    """Iterative inorder using stack."""
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process current node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result

def preorder_traversal(root):
    """Preorder traversal: root, left, right."""
    result = []
    
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return result

def postorder_traversal(root):
    """Postorder traversal: left, right, root."""
    result = []
    
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
    
    postorder(root)
    return result

# ============================================================================
# PROBLEM 2: LEVEL ORDER TRAVERSAL
# ============================================================================
def level_order(root):
    """
    Problem: Traverse tree level by level.
    
    Approach: BFS using queue
    Time Complexity: O(n)
    Space Complexity: O(w) where w is maximum width
    
    Example: [3,9,20,null,null,15,7] → [[3],[9,20],[15,7]]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

def zigzag_level_order(root):
    """
    Problem: Level order traversal in zigzag pattern.
    
    Example: [3,9,20,null,null,15,7] → [[3],[20,9],[15,7]]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if not left_to_right:
            current_level.reverse()
        
        result.append(current_level)
        left_to_right = not left_to_right
    
    return result

# ============================================================================
# PROBLEM 3: MAXIMUM DEPTH OF BINARY TREE
# ============================================================================
def max_depth(root):
    """
    Problem: Find maximum depth of binary tree.
    
    Approach: Recursive DFS
    Time Complexity: O(n)
    Space Complexity: O(h)
    
    Example: [3,9,20,null,null,15,7] → 3
    """
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))

def max_depth_iterative(root):
    """Iterative approach using level order traversal."""
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth

# ============================================================================
# PROBLEM 4: VALIDATE BINARY SEARCH TREE
# ============================================================================
def is_valid_bst(root):
    """
    Problem: Check if binary tree is valid BST.
    
    Approach: Inorder traversal should be sorted
    Time Complexity: O(n)
    Space Complexity: O(h)
    
    Example: [2,1,3] → True, [5,1,4,null,null,3,6] → False
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

def is_valid_bst_inorder(root):
    """Alternative: Check if inorder traversal is sorted."""
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    values = inorder(root)
    return all(values[i] < values[i + 1] for i in range(len(values) - 1))

# ============================================================================
# PROBLEM 5: SAME TREE
# ============================================================================
def is_same_tree(p, q):
    """
    Problem: Check if two binary trees are identical.
    
    Approach: Recursive comparison
    Time Complexity: O(min(m, n))
    Space Complexity: O(min(m, n))
    """
    # Both are None
    if not p and not q:
        return True
    
    # One is None, other is not
    if not p or not q:
        return False
    
    # Values are different
    if p.val != q.val:
        return False
    
    # Recursively check subtrees
    return (is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))

# ============================================================================
# PROBLEM 6: SYMMETRIC TREE
# ============================================================================
def is_symmetric(root):
    """
    Problem: Check if binary tree is symmetric (mirror of itself).
    
    Approach: Recursive helper function
    Time Complexity: O(n)
    Space Complexity: O(h)
    
    Example: [1,2,2,3,4,4,3] → True
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    return not root or is_mirror(root.left, root.right)

# ============================================================================
# PROBLEM 7: BINARY TREE PATHS
# ============================================================================
def binary_tree_paths(root):
    """
    Problem: Find all root-to-leaf paths.
    
    Approach: DFS with path tracking
    Time Complexity: O(n)
    Space Complexity: O(n * h)
    
    Example: [1,2,3,null,5] → ["1->2->5","1->3"]
    """
    if not root:
        return []
    
    paths = []
    
    def dfs(node, current_path):
        if not node:
            return
        
        current_path.append(str(node.val))
        
        # If leaf node, add path to result
        if not node.left and not node.right:
            paths.append("->".join(current_path))
        else:
            # Continue exploring
            dfs(node.left, current_path)
            dfs(node.right, current_path)
        
        # Backtrack
        current_path.pop()
    
    dfs(root, [])
    return paths

# ============================================================================
# PROBLEM 8: LOWEST COMMON ANCESTOR
# ============================================================================
def lowest_common_ancestor(root, p, q):
    """
    Problem: Find lowest common ancestor of two nodes.
    
    Approach: Recursive search
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    # If both left and right are not None, root is LCA
    if left and right:
        return root
    
    # Return the non-None child
    return left or right

def lca_bst(root, p, q):
    """
    LCA in BST - optimized version.
    Time Complexity: O(h), Space Complexity: O(1)
    """
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None

# ============================================================================
# PROBLEM 9: DIAMETER OF BINARY TREE
# ============================================================================
def diameter_of_binary_tree(root):
    """
    Problem: Find diameter (longest path between any two nodes).
    
    Approach: Calculate height while tracking max diameter
    Time Complexity: O(n)
    Space Complexity: O(h)
    
    Example: [1,2,3,4,5] → 3 (path 4->2->1->3 or 5->2->1->3)
    """
    max_diameter = 0
    
    def height(node):
        nonlocal max_diameter
        
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        # Update diameter through current node
        max_diameter = max(max_diameter, left_height + right_height)
        
        return 1 + max(left_height, right_height)
    
    height(root)
    return max_diameter

# ============================================================================
# PROBLEM 10: BINARY TREE MAXIMUM PATH SUM
# ============================================================================
def max_path_sum(root):
    """
    Problem: Find maximum path sum between any two nodes.
    
    Approach: Post-order traversal with path sum calculation
    Time Complexity: O(n)
    Space Complexity: O(h)
    
    Example: [1,2,3] → 6 (2->1->3)
    """
    max_sum = float('-inf')
    
    def max_gain(node):
        nonlocal max_sum
        
        if not node:
            return 0
        
        # Max gain from left and right subtrees (ignore negative gains)
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Path sum through current node
        current_max = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_max)
        
        # Return max gain including current node
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return max_sum

# ============================================================================
# PROBLEM 11: CONSTRUCT BINARY TREE FROM TRAVERSALS
# ============================================================================
def build_tree_preorder_inorder(preorder, inorder):
    """
    Problem: Build binary tree from preorder and inorder traversals.
    
    Approach: Use preorder for root, inorder for left/right subtrees
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not preorder or not inorder:
        return None
    
    # First element in preorder is root
    root = TreeNode(preorder[0])
    
    # Find root position in inorder
    mid = inorder.index(preorder[0])
    
    # Build left and right subtrees
    root.left = build_tree_preorder_inorder(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree_preorder_inorder(preorder[mid+1:], inorder[mid+1:])
    
    return root

def build_tree_inorder_postorder(inorder, postorder):
    """Build tree from inorder and postorder traversals."""
    if not inorder or not postorder:
        return None
    
    # Last element in postorder is root
    root = TreeNode(postorder[-1])
    
    # Find root position in inorder
    mid = inorder.index(postorder[-1])
    
    # Build left and right subtrees
    root.left = build_tree_inorder_postorder(inorder[:mid], postorder[:mid])
    root.right = build_tree_inorder_postorder(inorder[mid+1:], postorder[mid:-1])
    
    return root

# ============================================================================
# PROBLEM 12: SERIALIZE AND DESERIALIZE BINARY TREE
# ============================================================================
def serialize(root):
    """
    Problem: Serialize binary tree to string.
    
    Approach: Preorder traversal with null markers
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def preorder(node):
        if not node:
            vals.append("null")
        else:
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
    
    vals = []
    preorder(root)
    return ",".join(vals)

def deserialize(data):
    """Deserialize string back to binary tree."""
    def build():
        val = next(vals)
        if val == "null":
            return None
        
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node
    
    vals = iter(data.split(","))
    return build()

# ============================================================================
# PROBLEM 13: FLATTEN BINARY TREE TO LINKED LIST
# ============================================================================
def flatten(root):
    """
    Problem: Flatten binary tree to linked list in-place.
    
    Approach: Modified preorder traversal
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not root:
        return
    
    current = root
    
    while current:
        if current.left:
            # Find rightmost node in left subtree
            rightmost = current.left
            while rightmost.right:
                rightmost = rightmost.right
            
            # Connect rightmost to current's right
            rightmost.right = current.right
            
            # Move left subtree to right
            current.right = current.left
            current.left = None
        
        current = current.right

# ============================================================================
# PROBLEM 14: BINARY TREE RIGHT SIDE VIEW
# ============================================================================
def right_side_view(root):
    """
    Problem: Return values of nodes you can see from right side.
    
    Approach: Level order traversal, take last node of each level
    Time Complexity: O(n)
    Space Complexity: O(w)
    
    Example: [1,2,3,null,5,null,4] → [1,3,4]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # If last node in level, add to result
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# ============================================================================
# PROBLEM 15: KTHSMALLEST ELEMENT IN BST
# ============================================================================
def kth_smallest(root, k):
    """
    Problem: Find kth smallest element in BST.
    
    Approach: Inorder traversal (gives sorted order)
    Time Complexity: O(h + k)
    Space Complexity: O(h)
    """
    def inorder(node):
        if not node:
            return None
        
        # Search in left subtree
        left_result = inorder(node.left)
        if left_result is not None:
            return left_result
        
        # Process current node
        nonlocal k
        k -= 1
        if k == 0:
            return node.val
        
        # Search in right subtree
        return inorder(node.right)
    
    return inorder(root)

# ============================================================================
# PROBLEM 16: CONVERT BST TO GREATER TREE
# ============================================================================
def convert_bst(root):
    """
    Problem: Convert BST where each node's value is sum of all greater values.
    
    Approach: Reverse inorder traversal (right, root, left)
    Time Complexity: O(n)
    Space Complexity: O(h)
    
    Example: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8] 
             → [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
    """
    total = 0
    
    def reverse_inorder(node):
        nonlocal total
        
        if node:
            reverse_inorder(node.right)
            total += node.val
            node.val = total
            reverse_inorder(node.left)
    
    reverse_inorder(root)
    return root

# ============================================================================
# TEST FUNCTIONS
# ============================================================================
def create_test_tree():
    """Create a test binary tree: [3,9,20,null,null,15,7]"""
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def test_binary_tree_problems():
    """Test all binary tree problems with examples."""
    
    print("=== BINARY TREE PROBLEMS & SOLUTIONS ===\n")
    
    # Create test tree
    root = create_test_tree()
    
    # Test 1: Tree Traversals
    print("1. BINARY TREE TRAVERSALS")
    print(f"Inorder: {inorder_traversal(root)}")
    print(f"Preorder: {preorder_traversal(root)}")
    print(f"Postorder: {postorder_traversal(root)}")
    print(f"Level order: {level_order(root)}")
    print(f"Zigzag level order: {zigzag_level_order(root)}")
    
    # Test 2: Maximum Depth
    print("\n2. MAXIMUM DEPTH")
    print(f"Max depth: {max_depth(root)}")
    
    # Test 3: Validate BST
    print("\n3. VALIDATE BST")
    bst = TreeNode(2)
    bst.left = TreeNode(1)
    bst.right = TreeNode(3)
    print(f"Is valid BST: {is_valid_bst(bst)}")
    
    # Test 4: Same Tree
    print("\n4. SAME TREE")
    root2 = create_test_tree()
    print(f"Trees are same: {is_same_tree(root, root2)}")
    
    # Test 5: Symmetric Tree
    print("\n5. SYMMETRIC TREE")
    sym_root = TreeNode(1)
    sym_root.left = TreeNode(2)
    sym_root.right = TreeNode(2)
    sym_root.left.left = TreeNode(3)
    sym_root.left.right = TreeNode(4)
    sym_root.right.left = TreeNode(4)
    sym_root.right.right = TreeNode(3)
    print(f"Is symmetric: {is_symmetric(sym_root)}")
    
    # Test 6: Binary Tree Paths
    print("\n6. BINARY TREE PATHS")
    small_tree = TreeNode(1)
    small_tree.left = TreeNode(2)
    small_tree.right = TreeNode(3)
    small_tree.left.right = TreeNode(5)
    print(f"All paths: {binary_tree_paths(small_tree)}")
    
    # Test 7: Diameter
    print("\n7. DIAMETER OF BINARY TREE")
    print(f"Diameter: {diameter_of_binary_tree(root)}")
    
    # Test 8: Maximum Path Sum
    print("\n8. MAXIMUM PATH SUM")
    print(f"Max path sum: {max_path_sum(root)}")
    
    # Test 9: Right Side View
    print("\n9. RIGHT SIDE VIEW")
    print(f"Right side view: {right_side_view(root)}")
    
    # Test 10: Serialize/Deserialize
    print("\n10. SERIALIZE/DESERIALIZE")
    serialized = serialize(root)
    print(f"Serialized: {serialized}")
    deserialized = deserialize(serialized)
    print(f"Deserialized same as original: {is_same_tree(root, deserialized)}")

if __name__ == "__main__":
    test_binary_tree_problems()