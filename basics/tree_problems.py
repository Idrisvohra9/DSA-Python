"""
TREE PROBLEMS & SOLUTIONS
=========================
Collection of well-known tree problems with optimal solutions.
This includes general tree problems, N-ary trees, and advanced tree algorithms
beyond binary trees.
"""

from collections import deque, defaultdict
import heapq

# ============================================================================
# N-ARY TREE NODE DEFINITIONS
# ============================================================================
class TreeNode:
    """N-ary tree node definition."""
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

class TrieNode:
    """Trie (Prefix Tree) node definition."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# ============================================================================
# PROBLEM 1: N-ARY TREE TRAVERSALS
# ============================================================================
def preorder_nary(root):
    """
    Problem: Preorder traversal of N-ary tree.
    
    Approach: Recursive DFS
    Time Complexity: O(n)
    Space Complexity: O(h)
    
    Example: [1,null,3,2,4,null,5,6] → [1,3,5,6,2,4]
    """
    if not root:
        return []
    
    result = [root.val]
    for child in root.children:
        result.extend(preorder_nary(child))
    
    return result

def preorder_nary_iterative(root):
    """Iterative preorder using stack."""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Add children in reverse order for correct processing
        for child in reversed(node.children):
            stack.append(child)
    
    return result

def postorder_nary(root):
    """
    Problem: Postorder traversal of N-ary tree.
    Visit children first, then root.
    """
    if not root:
        return []
    
    result = []
    for child in root.children:
        result.extend(postorder_nary(child))
    result.append(root.val)
    
    return result

def level_order_nary(root):
    """
    Problem: Level order traversal of N-ary tree.
    
    Approach: BFS using queue
    Time Complexity: O(n)
    Space Complexity: O(w) where w is maximum width
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
            
            for child in node.children:
                queue.append(child)
        
        result.append(current_level)
    
    return result

# ============================================================================
# PROBLEM 2: MAXIMUM DEPTH OF N-ARY TREE
# ============================================================================
def max_depth_nary(root):
    """
    Problem: Find maximum depth of N-ary tree.
    
    Approach: Recursive DFS
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    if not root:
        return 0
    
    if not root.children:
        return 1
    
    return 1 + max(max_depth_nary(child) for child in root.children)

def max_depth_nary_iterative(root):
    """Iterative approach using level order traversal."""
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        for child in node.children:
            queue.append((child, depth + 1))
    
    return max_depth

# ============================================================================
# PROBLEM 3: TRIE (PREFIX TREE) IMPLEMENTATION
# ============================================================================
class Trie:
    """
    Problem: Implement Trie data structure for string storage and search.
    
    Operations: insert, search, startsWith
    Time Complexity: O(m) for all operations where m is key length
    Space Complexity: O(ALPHABET_SIZE * N * M)
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert word into trie."""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word):
        """Search for exact word in trie."""
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if any word starts with given prefix."""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
    
    def get_all_words_with_prefix(self, prefix):
        """Get all words that start with given prefix."""
        def dfs(node, current_word):
            if node.is_end_of_word:
                words.append(current_word)
            
            for char, child_node in node.children.items():
                dfs(child_node, current_word + char)
        
        # Find prefix node
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all words from prefix node
        words = []
        dfs(node, prefix)
        return words

# ============================================================================
# PROBLEM 4: WORD SEARCH II (TRIE + BACKTRACKING)
# ============================================================================
def find_words(board, words):
    """
    Problem: Find all words from dictionary that exist in 2D board.
    
    Approach: Trie + DFS backtracking
    Time Complexity: O(M * N * 4^L) where L is max word length
    Space Complexity: O(W * L) for trie where W is number of words
    
    Example: board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
             words=["oath","pea","eat","rain"] → ["eat","oath"]
    """
    # Build trie from words
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    rows, cols = len(board), len(board[0])
    result = set()
    
    def dfs(row, col, node, current_word):
        # Check bounds and if cell was visited
        if (row < 0 or row >= rows or col < 0 or col >= cols or
            board[row][col] == '#' or board[row][col] not in node.children):
            return
        
        # Get current character and move to next node
        char = board[row][col]
        node = node.children[char]
        current_word += char
        
        # If we found a word, add to result
        if node.is_end_of_word:
            result.add(current_word)
        
        # Mark cell as visited
        board[row][col] = '#'
        
        # Explore all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            dfs(row + dr, col + dc, node, current_word)
        
        # Backtrack: restore original character
        board[row][col] = char
    
    # Start DFS from each cell
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, trie.root, "")
    
    return list(result)

# ============================================================================
# PROBLEM 5: LOWEST COMMON ANCESTOR IN N-ARY TREE
# ============================================================================
def lowest_common_ancestor_nary(root, nodes):
    """
    Problem: Find LCA of multiple nodes in N-ary tree.
    
    Approach: DFS with node tracking
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    def dfs(node):
        if not node:
            return 0, None
        
        # Count how many target nodes found in current subtree
        found_count = 1 if node in nodes else 0
        
        for child in node.children:
            child_count, child_lca = dfs(child)
            found_count += child_count
            
            # If child subtree contains all nodes, return its LCA
            if child_lca:
                return found_count, child_lca
        
        # If current node's subtree contains all target nodes
        if found_count == len(nodes):
            return found_count, node
        
        return found_count, None
    
    _, lca = dfs(root)
    return lca

# ============================================================================
# PROBLEM 6: DIAMETER OF N-ARY TREE
# ============================================================================
def diameter_nary(root):
    """
    Problem: Find diameter of N-ary tree (longest path between any two nodes).
    
    Approach: For each node, find two longest paths and combine
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    max_diameter = 0
    
    def dfs(node):
        nonlocal max_diameter
        
        if not node:
            return 0
        
        # Get depths of all children
        depths = []
        for child in node.children:
            depths.append(dfs(child))
        
        # Sort to get two largest depths
        depths.sort(reverse=True)
        
        # Diameter through current node
        if len(depths) >= 2:
            current_diameter = depths[0] + depths[1]
        elif len(depths) == 1:
            current_diameter = depths[0]
        else:
            current_diameter = 0
        
        max_diameter = max(max_diameter, current_diameter)
        
        # Return depth of current subtree
        return 1 + (depths[0] if depths else 0)
    
    dfs(root)
    return max_diameter

# ============================================================================
# PROBLEM 7: SERIALIZE AND DESERIALIZE N-ARY TREE
# ============================================================================
def serialize_nary(root):
    """
    Problem: Serialize N-ary tree to string.
    
    Approach: Preorder with children count
    Format: "val,children_count,child1,child2,..."
    """
    if not root:
        return ""
    
    def preorder(node):
        if not node:
            return
        
        # Add node value and children count
        vals.append(str(node.val))
        vals.append(str(len(node.children)))
        
        # Add all children
        for child in node.children:
            preorder(child)
    
    vals = []
    preorder(root)
    return ",".join(vals)

def deserialize_nary(data):
    """Deserialize string back to N-ary tree."""
    if not data:
        return None
    
    vals = iter(data.split(","))
    
    def build():
        try:
            val = int(next(vals))
            children_count = int(next(vals))
            
            node = TreeNode(val)
            for _ in range(children_count):
                child = build()
                if child:
                    node.children.append(child)
            
            return node
        except StopIteration:
            return None
    
    return build()

# ============================================================================
# PROBLEM 8: CLONE N-ARY TREE
# ============================================================================
def clone_tree(root):
    """
    Problem: Deep clone N-ary tree.
    
    Approach: DFS with node creation
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    if not root:
        return None
    
    # Create new node
    cloned = TreeNode(root.val)
    
    # Clone all children
    for child in root.children:
        cloned_child = clone_tree(child)
        cloned.children.append(cloned_child)
    
    return cloned

# ============================================================================
# PROBLEM 9: FIND DUPLICATE SUBTREES
# ============================================================================
def find_duplicate_subtrees_nary(root):
    """
    Problem: Find all duplicate subtrees in N-ary tree.
    
    Approach: Serialize each subtree and count occurrences
    Time Complexity: O(n²)
    Space Complexity: O(n²)
    """
    def serialize(node):
        if not node:
            return "null"
        
        # Serialize current subtree
        subtree = str(node.val) + "(" + ",".join(serialize(child) for child in node.children) + ")"
        
        # Count occurrences
        count[subtree] += 1
        if count[subtree] == 2:  # First time seeing duplicate
            duplicates.append(node)
        
        return subtree
    
    count = defaultdict(int)
    duplicates = []
    serialize(root)
    return duplicates

# ============================================================================
# PROBLEM 10: TREE ISOMORPHISM
# ============================================================================
def are_isomorphic(root1, root2):
    """
    Problem: Check if two trees are isomorphic (same structure).
    
    Approach: Compare structures recursively
    Time Complexity: O(min(n1, n2))
    Space Complexity: O(h)
    """
    # Both empty
    if not root1 and not root2:
        return True
    
    # One empty, other not
    if not root1 or not root2:
        return False
    
    # Different number of children
    if len(root1.children) != len(root2.children):
        return False
    
    # Check all children (order matters for isomorphism)
    for child1, child2 in zip(root1.children, root2.children):
        if not are_isomorphic(child1, child2):
            return False
    
    return True

# ============================================================================
# PROBLEM 11: VERTICAL ORDER TRAVERSAL
# ============================================================================
def vertical_order(root):
    """
    Problem: Return vertical order traversal of tree.
    
    Approach: BFS with column tracking
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not root:
        return []
    
    column_map = defaultdict(list)
    queue = deque([(root, 0)])  # (node, column)
    
    while queue:
        node, col = queue.popleft()
        column_map[col].append(node.val)
        
        # Add children with updated column positions
        for i, child in enumerate(node.children):
            # Adjust column based on child position
            child_col = col + i - len(node.children) // 2
            queue.append((child, child_col))
    
    # Sort by column and return values
    result = []
    for col in sorted(column_map.keys()):
        result.extend(column_map[col])
    
    return result

# ============================================================================
# PROBLEM 12: PATH SUM IN TREE
# ============================================================================
def has_path_sum_nary(root, target_sum):
    """
    Problem: Check if there's a root-to-leaf path with given sum.
    
    Approach: DFS with sum tracking
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    if not root:
        return False
    
    # If leaf node, check if sum matches
    if not root.children:
        return root.val == target_sum
    
    # Check all children with reduced sum
    remaining_sum = target_sum - root.val
    for child in root.children:
        if has_path_sum_nary(child, remaining_sum):
            return True
    
    return False

def path_sum_all_paths(root, target_sum):
    """Find all root-to-leaf paths with given sum."""
    def dfs(node, current_sum, current_path):
        if not node:
            return
        
        current_path.append(node.val)
        current_sum += node.val
        
        # If leaf node and sum matches
        if not node.children and current_sum == target_sum:
            paths.append(current_path[:])
        
        # Continue with children
        for child in node.children:
            dfs(child, current_sum, current_path)
        
        # Backtrack
        current_path.pop()
    
    paths = []
    dfs(root, 0, [])
    return paths

# ============================================================================
# TEST FUNCTIONS
# ============================================================================
def create_test_nary_tree():
    """Create test N-ary tree: [1,null,3,2,4,null,5,6]"""
    root = TreeNode(1)
    root.children = [TreeNode(3), TreeNode(2), TreeNode(4)]
    root.children[0].children = [TreeNode(5), TreeNode(6)]
    return root

def test_tree_problems():
    """Test all tree problems with examples."""
    
    print("=== TREE PROBLEMS & SOLUTIONS ===\n")
    
    # Create test N-ary tree
    root = create_test_nary_tree()
    
    # Test 1: N-ary Tree Traversals
    print("1. N-ARY TREE TRAVERSALS")
    print(f"Preorder: {preorder_nary(root)}")
    print(f"Postorder: {postorder_nary(root)}")
    print(f"Level order: {level_order_nary(root)}")
    
    # Test 2: Maximum Depth
    print("\n2. MAXIMUM DEPTH OF N-ARY TREE")
    print(f"Max depth: {max_depth_nary(root)}")
    
    # Test 3: Trie Operations
    print("\n3. TRIE (PREFIX TREE)")
    trie = Trie()
    words = ["apple", "app", "apricot", "banana"]
    for word in words:
        trie.insert(word)
    
    print(f"Inserted words: {words}")
    print(f"Search 'app': {trie.search('app')}")
    print(f"Search 'appl': {trie.search('appl')}")
    print(f"Starts with 'app': {trie.starts_with('app')}")
    print(f"Words with prefix 'app': {trie.get_all_words_with_prefix('app')}")
    
    # Test 4: Diameter of N-ary Tree
    print("\n4. DIAMETER OF N-ARY TREE")
    print(f"Diameter: {diameter_nary(root)}")
    
    # Test 5: Serialize/Deserialize
    print("\n5. SERIALIZE/DESERIALIZE N-ARY TREE")
    serialized = serialize_nary(root)
    print(f"Serialized: {serialized}")
    deserialized = deserialize_nary(serialized)
    print(f"Deserialized preorder: {preorder_nary(deserialized)}")
    
    # Test 6: Clone Tree
    print("\n6. CLONE N-ARY TREE")
    cloned = clone_tree(root)
    print(f"Original preorder: {preorder_nary(root)}")
    print(f"Cloned preorder: {preorder_nary(cloned)}")
    print(f"Are isomorphic: {are_isomorphic(root, cloned)}")
    
    # Test 7: Path Sum
    print("\n7. PATH SUM IN TREE")
    # Create simple tree for path sum test
    simple_root = TreeNode(5)
    simple_root.children = [TreeNode(4), TreeNode(8)]
    simple_root.children[0].children = [TreeNode(11)]
    simple_root.children[1].children = [TreeNode(13), TreeNode(4)]
    
    target = 20
    print(f"Has path sum {target}: {has_path_sum_nary(simple_root, target)}")
    print(f"All paths with sum {target}: {path_sum_all_paths(simple_root, target)}")

if __name__ == "__main__":
    test_tree_problems()