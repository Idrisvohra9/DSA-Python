"""
QUEUE PROBLEMS & SOLUTIONS
=========================
Collection of well-known queue problems with optimal solutions.
Queue follows FIFO (First In, First Out) principle - perfect for problems involving
level-order traversal, scheduling, and breadth-first search.
"""

from collections import deque

# ============================================================================
# PROBLEM 1: IMPLEMENT STACK USING QUEUES
# ============================================================================
class MyStack:
    """
    Problem: Implement stack using only queues.
    
    Approach: Use single queue, rotate elements during push
    Time Complexity: O(n) for push, O(1) for pop
    Space Complexity: O(n)
    """
    
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        """Add element to top of stack."""
        self.queue.append(x)
        # Rotate all previous elements to make new element first
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        """Remove top element from stack."""
        return self.queue.popleft()
    
    def top(self):
        """Get top element without removing."""
        return self.queue[0]
    
    def empty(self):
        """Check if stack is empty."""
        return not self.queue

# ============================================================================
# PROBLEM 2: SLIDING WINDOW MAXIMUM
# ============================================================================
def max_sliding_window(nums, k):
    """
    Problem: Find maximum in each sliding window of size k.
    
    Approach: Monotonic decreasing deque
    Time Complexity: O(n)
    Space Complexity: O(k)
    
    Example: nums=[1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7]
    """
    if not nums or k == 0:
        return []
    
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove indices of smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# ============================================================================
# PROBLEM 3: BINARY TREE LEVEL ORDER TRAVERSAL
# ============================================================================
class TreeNode:
    """Binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    """
    Problem: Traverse binary tree level by level.
    
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
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# ============================================================================
# PROBLEM 4: BINARY TREE ZIGZAG LEVEL ORDER TRAVERSAL
# ============================================================================
def zigzag_level_order(root):
    """
    Problem: Traverse binary tree in zigzag pattern (left-right, right-left).
    
    Approach: BFS with alternating direction
    Time Complexity: O(n)
    Space Complexity: O(w)
    
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
        
        # Reverse if going right to left
        if not left_to_right:
            current_level.reverse()
        
        result.append(current_level)
        left_to_right = not left_to_right
    
    return result

# ============================================================================
# PROBLEM 5: ROTTING ORANGES
# ============================================================================
def oranges_rotting(grid):
    """
    Problem: Find minimum time for all oranges to rot.
    Fresh oranges adjacent to rotten ones rot in 1 minute.
    
    Approach: Multi-source BFS
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    
    Example: [[2,1,1],[1,1,0],[0,1,1]] → 4 minutes
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    # Find all rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:
                fresh_count += 1
    
    # If no fresh oranges, return 0
    if fresh_count == 0:
        return 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_time = 0
    
    while queue:
        row, col, time = queue.popleft()
        max_time = max(max_time, time)
        
        # Check all 4 directions
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            
            # If valid position and fresh orange
            if (0 <= nr < rows and 0 <= nc < cols and 
                grid[nr][nc] == 1):
                
                grid[nr][nc] = 2  # Mark as rotten
                fresh_count -= 1
                queue.append((nr, nc, time + 1))
    
    # Return time if all oranges rotted, else -1
    return max_time if fresh_count == 0 else -1

# ============================================================================
# PROBLEM 6: PERFECT SQUARES
# ============================================================================
def num_squares(n):
    """
    Problem: Find minimum number of perfect squares that sum to n.
    
    Approach: BFS to find shortest path
    Time Complexity: O(n * sqrt(n))
    Space Complexity: O(n)
    
    Example: n=12 → 3 (4+4+4)
    """
    if n <= 0:
        return 0
    
    # Generate perfect squares up to n
    perfect_squares = []
    i = 1
    while i * i <= n:
        perfect_squares.append(i * i)
        i += 1
    
    # BFS to find minimum steps
    queue = deque([n])
    visited = {n}
    level = 0
    
    while queue:
        level += 1
        for _ in range(len(queue)):
            remainder = queue.popleft()
            
            # Try subtracting each perfect square
            for square in perfect_squares:
                if square > remainder:
                    break
                
                if square == remainder:
                    return level
                
                if remainder - square not in visited:
                    visited.add(remainder - square)
                    queue.append(remainder - square)
    
    return level

# ============================================================================
# PROBLEM 7: WALLS AND GATES
# ============================================================================
def walls_and_gates(rooms):
    """
    Problem: Fill rooms with distance to nearest gate.
    -1: wall, 0: gate, INF: empty room
    
    Approach: Multi-source BFS from all gates
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    if not rooms or not rooms[0]:
        return
    
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()
    INF = 2**31 - 1
    
    # Find all gates
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        row, col = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            
            # If valid position and empty room
            if (0 <= nr < rows and 0 <= nc < cols and 
                rooms[nr][nc] == INF):
                
                rooms[nr][nc] = rooms[row][col] + 1
                queue.append((nr, nc))

# ============================================================================
# PROBLEM 8: SHORTEST PATH IN BINARY MATRIX
# ============================================================================
def shortest_path_binary_matrix(grid):
    """
    Problem: Find shortest path from top-left to bottom-right in binary matrix.
    0: open cell, 1: blocked cell. Can move in 8 directions.
    
    Approach: BFS shortest path
    Time Complexity: O(n²)
    Space Complexity: O(n²)
    """
    n = len(grid)
    
    # Check if start or end is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Special case: single cell
    if n == 1:
        return 1
    
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = {(0, 0)}
    
    # 8 directions
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    while queue:
        row, col, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            
            # Check bounds and if cell is open and unvisited
            if (0 <= nr < n and 0 <= nc < n and 
                grid[nr][nc] == 0 and (nr, nc) not in visited):
                
                # Check if reached destination
                if nr == n - 1 and nc == n - 1:
                    return dist + 1
                
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return -1

# ============================================================================
# PROBLEM 9: OPEN THE LOCK
# ============================================================================
def open_lock(deadends, target):
    """
    Problem: Find minimum steps to reach target combination on 4-digit lock.
    Can rotate each digit up or down. Avoid deadend combinations.
    
    Approach: BFS with bidirectional search
    Time Complexity: O(10^4)
    Space Complexity: O(10^4)
    """
    if "0000" in deadends:
        return -1
    if target == "0000":
        return 0
    
    deadends = set(deadends)
    
    # Bidirectional BFS
    start_set = {"0000"}
    end_set = {target}
    visited = set(deadends)
    steps = 0
    
    def get_neighbors(combination):
        """Get all possible next combinations."""
        neighbors = []
        for i in range(4):
            digit = int(combination[i])
            # Rotate up
            new_combo = combination[:i] + str((digit + 1) % 10) + combination[i+1:]
            neighbors.append(new_combo)
            # Rotate down
            new_combo = combination[:i] + str((digit - 1) % 10) + combination[i+1:]
            neighbors.append(new_combo)
        return neighbors
    
    while start_set and end_set:
        # Always expand smaller set
        if len(start_set) > len(end_set):
            start_set, end_set = end_set, start_set
        
        next_set = set()
        
        for combination in start_set:
            for neighbor in get_neighbors(combination):
                if neighbor in end_set:
                    return steps + 1
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_set.add(neighbor)
        
        start_set = next_set
        steps += 1
    
    return -1

# ============================================================================
# PROBLEM 10: COURSE SCHEDULE II
# ============================================================================
def find_order(num_courses, prerequisites):
    """
    Problem: Find valid order to take all courses given prerequisites.
    
    Approach: Topological sort using BFS (Kahn's algorithm)
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    
    Example: numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]] → [0,1,2,3]
    """
    # Build graph and in-degree count
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Start with courses having no prerequisites
    queue = deque()
    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = []
    
    while queue:
        course = queue.popleft()
        result.append(course)
        
        # Remove this course and update in-degrees
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all courses can be taken
    return result if len(result) == num_courses else []

# ============================================================================
# PROBLEM 11: DESIGN HIT COUNTER
# ============================================================================
class HitCounter:
    """
    Problem: Design hit counter that counts hits in past 5 minutes.
    
    Approach: Queue with timestamps
    Time Complexity: O(1) amortized for hit, O(s) for getHits where s is hits in window
    Space Complexity: O(s)
    """
    
    def __init__(self):
        self.hits = deque()  # Store timestamps
    
    def hit(self, timestamp):
        """Record a hit at given timestamp."""
        self.hits.append(timestamp)
    
    def get_hits(self, timestamp):
        """Get number of hits in past 300 seconds."""
        # Remove hits older than 300 seconds
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        
        return len(self.hits)

# ============================================================================
# PROBLEM 12: MOVING AVERAGE FROM DATA STREAM
# ============================================================================
class MovingAverage:
    """
    Problem: Calculate moving average of last n numbers in data stream.
    
    Approach: Circular buffer using queue
    Time Complexity: O(1)
    Space Complexity: O(n)
    """
    
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.total = 0
    
    def next(self, val):
        """Add new value and return moving average."""
        self.queue.append(val)
        self.total += val
        
        # Remove oldest value if window exceeded
        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.total -= removed
        
        return self.total / len(self.queue)

# ============================================================================
# TEST FUNCTIONS
# ============================================================================
def test_queue_problems():
    """Test all queue problems with examples."""
    
    print("=== QUEUE PROBLEMS & SOLUTIONS ===\n")
    
    # Test 1: Implement Stack Using Queues
    print("1. IMPLEMENT STACK USING QUEUES")
    stack = MyStack()
    operations = ["push(1)", "push(2)", "top()", "pop()", "empty()"]
    stack.push(1)
    stack.push(2)
    print(f"Operations: {operations}")
    print(f"Top: {stack.top()}, Pop: {stack.pop()}, Empty: {stack.empty()}")
    
    # Test 2: Sliding Window Maximum
    print("\n2. SLIDING WINDOW MAXIMUM")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Array: {nums}, Window size: {k}")
    print(f"Maximums: {max_sliding_window(nums, k)}")
    
    # Test 3: Binary Tree Level Order Traversal
    print("\n3. BINARY TREE LEVEL ORDER TRAVERSAL")
    # Create tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(f"Level order: {level_order(root)}")
    print(f"Zigzag order: {zigzag_level_order(root)}")
    
    # Test 4: Rotting Oranges
    print("\n4. ROTTING ORANGES")
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print("Grid:", grid)
    print(f"Minutes to rot all: {oranges_rotting(grid)}")
    
    # Test 5: Perfect Squares
    print("\n5. PERFECT SQUARES")
    for n in [12, 13, 1]:
        print(f"n={n} → {num_squares(n)} perfect squares")
    
    # Test 6: Shortest Path in Binary Matrix
    print("\n6. SHORTEST PATH IN BINARY MATRIX")
    matrix = [[0,0,0],[1,1,0],[1,1,0]]
    print("Matrix:", matrix)
    print(f"Shortest path: {shortest_path_binary_matrix(matrix)}")
    
    # Test 7: Course Schedule
    print("\n7. COURSE SCHEDULE II")
    num_courses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(f"Courses: {num_courses}, Prerequisites: {prerequisites}")
    print(f"Order: {find_order(num_courses, prerequisites)}")
    
    # Test 8: Moving Average
    print("\n8. MOVING AVERAGE")
    ma = MovingAverage(3)
    values = [1, 10, 3, 5]
    print("Values and averages:")
    for val in values:
        avg = ma.next(val)
        print(f"  Add {val} → Average: {avg:.2f}")

if __name__ == "__main__":
    test_queue_problems()