"""
MAP (HASH MAP / DICTIONARY) PROBLEMS & SOLUTIONS
===============================================
Collection of well-known hash map problems with optimal solutions.
Hash maps provide O(1) average time complexity for insertions, deletions, and lookups,
making them essential for many algorithmic solutions.
"""

from collections import defaultdict, Counter
import heapq

# ============================================================================
# PROBLEM 1: GROUP ANAGRAMS
# ============================================================================
def group_anagrams(strs):
    """
    Problem: Group strings that are anagrams of each other.
    
    Approach: Use sorted string as key in hash map
    Time Complexity: O(n * k log k) where k is max string length
    Space Complexity: O(n * k)
    
    Example: ["eat","tea","tan","ate","nat","bat"] → [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Sort characters to create key
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())

def group_anagrams_optimized(strs):
    """
    Optimized version using character count as key.
    Time Complexity: O(n * k) where k is max string length
    """
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Create key from character counts
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())

# ============================================================================
# PROBLEM 2: VALID ANAGRAM
# ============================================================================
def is_anagram(s, t):
    """
    Problem: Check if two strings are anagrams.
    
    Approach: Compare character frequencies
    Time Complexity: O(n)
    Space Complexity: O(1) for lowercase letters
    
    Example: s="anagram", t="nagaram" → True
    """
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    # Count characters in first string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract characters from second string
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0

def is_anagram_counter(s, t):
    """Using Counter for cleaner implementation."""
    return Counter(s) == Counter(t)

# ============================================================================
# PROBLEM 3: TOP K FREQUENT ELEMENTS
# ============================================================================
def top_k_frequent(nums, k):
    """
    Problem: Find k most frequent elements in array.
    
    Approach: Hash map + heap
    Time Complexity: O(n log k)
    Space Complexity: O(n)
    
    Example: nums=[1,1,1,2,2,3], k=2 → [1,2]
    """
    # Count frequencies
    count = Counter(nums)
    
    # Use min heap to keep k most frequent
    heap = []
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for freq, num in heap]

def top_k_frequent_bucket_sort(nums, k):
    """
    Optimized version using bucket sort.
    Time Complexity: O(n), Space Complexity: O(n)
    """
    count = Counter(nums)
    
    # Create buckets for each frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in count.items():
        buckets[freq].append(num)
    
    # Collect k most frequent elements
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

# ============================================================================
# PROBLEM 4: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ============================================================================
def length_of_longest_substring(s):
    """
    Problem: Find length of longest substring without repeating characters.
    
    Approach: Sliding window with hash map
    Time Complexity: O(n)
    Space Complexity: O(min(m, n)) where m is charset size
    
    Example: s="abcabcbb" → 3 ("abc")
    """
    char_index = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If character seen before and within current window
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

# ============================================================================
# PROBLEM 5: FIND ALL ANAGRAMS IN A STRING
# ============================================================================
def find_anagrams(s, p):
    """
    Problem: Find all start indices of anagrams of p in s.
    
    Approach: Sliding window with character count
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: s="abab", p="ab" → [0,2]
    """
    if len(p) > len(s):
        return []
    
    result = []
    p_count = Counter(p)
    window_count = Counter()
    
    # Initialize window
    for i in range(len(p)):
        window_count[s[i]] += 1
    
    # Check first window
    if window_count == p_count:
        result.append(0)
    
    # Slide window
    for i in range(len(p), len(s)):
        # Add new character
        window_count[s[i]] += 1
        
        # Remove old character
        left_char = s[i - len(p)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        
        # Check if current window is anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

# ============================================================================
# PROBLEM 6: WORD PATTERN
# ============================================================================
def word_pattern(pattern, s):
    """
    Problem: Check if string follows given pattern.
    
    Approach: Bidirectional mapping
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: pattern="abba", s="dog cat cat dog" → True
    """
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        # Check char -> word mapping
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        # Check word -> char mapping
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True

# ============================================================================
# PROBLEM 7: ISOMORPHIC STRINGS
# ============================================================================
def is_isomorphic(s, t):
    """
    Problem: Check if two strings are isomorphic.
    
    Approach: Character mapping validation
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: s="egg", t="add" → True
    """
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        # Check s -> t mapping
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        # Check t -> s mapping
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True

# ============================================================================
# PROBLEM 8: MINIMUM WINDOW SUBSTRING
# ============================================================================
def min_window(s, t):
    """
    Problem: Find minimum window substring containing all characters of t.
    
    Approach: Sliding window with character count
    Time Complexity: O(|s| + |t|)
    Space Complexity: O(|s| + |t|)
    
    Example: s="ADOBECODEBANC", t="ABC" → "BANC"
    """
    if not s or not t or len(s) < len(t):
        return ""
    
    t_count = Counter(t)
    required = len(t_count)
    
    left = right = 0
    formed = 0
    window_counts = {}
    
    # Result tuple (window length, left, right)
    ans = float('inf'), None, None
    
    while right < len(s):
        # Add character from right
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # Check if current character satisfies requirement
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1
        
        # Try to contract window
        while left <= right and formed == required:
            char = s[left]
            
            # Update result if current window is smaller
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            # Remove from left
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

# ============================================================================
# PROBLEM 9: FIRST UNIQUE CHARACTER IN STRING
# ============================================================================
def first_uniq_char(s):
    """
    Problem: Find index of first non-repeating character.
    
    Approach: Two-pass with character count
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: s="leetcode" → 0 ('l')
    """
    char_count = Counter(s)
    
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1

# ============================================================================
# PROBLEM 10: SUBARRAY SUM EQUALS K
# ============================================================================
def subarray_sum_equals_k(nums, k):
    """
    Problem: Count subarrays with sum equal to k.
    
    Approach: Prefix sum with hash map
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: nums=[1,1,1], k=2 → 2
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # prefix_sum -> frequency
    
    for num in nums:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        # Update frequency
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count

# ============================================================================
# PROBLEM 11: COPY LIST WITH RANDOM POINTER
# ============================================================================
class Node:
    """Node with random pointer."""
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

def copy_random_list(head):
    """
    Problem: Deep copy linked list with random pointers.
    
    Approach: Hash map to store node mappings
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not head:
        return None
    
    # Create mapping of original -> copy nodes
    node_map = {}
    
    # First pass: create all nodes
    current = head
    while current:
        node_map[current] = Node(current.val)
        current = current.next
    
    # Second pass: set next and random pointers
    current = head
    while current:
        copy_node = node_map[current]
        if current.next:
            copy_node.next = node_map[current.next]
        if current.random:
            copy_node.random = node_map[current.random]
        current = current.next
    
    return node_map[head]

# ============================================================================
# PROBLEM 12: LRU CACHE
# ============================================================================
class LRUCache:
    """
    Problem: Implement Least Recently Used cache.
    
    Approach: Hash map + doubly linked list
    Time Complexity: O(1) for get and put
    Space Complexity: O(capacity)
    """
    
    class DListNode:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Create dummy head and tail
        self.head = self.DListNode()
        self.tail = self.DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """Add node right after head."""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Remove an existing node."""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """Move node to head (mark as recently used)."""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """Remove last node."""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node
    
    def get(self, key):
        """Get value and mark as recently used."""
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.val
        return -1
    
    def put(self, key, value):
        """Put key-value pair."""
        if key in self.cache:
            # Update existing
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            # Add new
            new_node = self.DListNode(key, value)
            
            if len(self.cache) >= self.capacity:
                # Remove LRU
                tail = self._pop_tail()
                del self.cache[tail.key]
            
            self.cache[key] = new_node
            self._add_node(new_node)

# ============================================================================
# PROBLEM 13: LONGEST CONSECUTIVE SEQUENCE
# ============================================================================
def longest_consecutive(nums):
    """
    Problem: Find length of longest consecutive sequence.
    
    Approach: Hash set for O(1) lookups
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: [100,4,200,1,3,2] → 4 ([1,2,3,4])
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Only start counting from the beginning of sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest = max(longest, current_streak)
    
    return longest

# ============================================================================
# PROBLEM 14: DESIGN TWITTER
# ============================================================================
import heapq
from collections import defaultdict

class Twitter:
    """
    Problem: Design simplified Twitter with follow, unfollow, post, getNewsFeed.
    
    Approach: Hash maps for users/tweets + heap for timeline
    """
    
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # user_id -> [(time, tweet_id)]
        self.following = defaultdict(set)  # user_id -> set of followee_ids
    
    def post_tweet(self, user_id, tweet_id):
        """Post a tweet."""
        self.tweets[user_id].append((self.time, tweet_id))
        self.time += 1
    
    def get_news_feed(self, user_id):
        """Get 10 most recent tweets from user and their followees."""
        # Get all relevant users
        users = self.following[user_id] | {user_id}
        
        # Use max heap to get most recent tweets
        heap = []
        
        for u in users:
            if u in self.tweets and self.tweets[u]:
                # Add most recent tweet from this user
                time, tweet_id = self.tweets[u][-1]
                heapq.heappush(heap, (-time, tweet_id, u, len(self.tweets[u]) - 1))
        
        result = []
        while heap and len(result) < 10:
            neg_time, tweet_id, u, index = heapq.heappop(heap)
            result.append(tweet_id)
            
            # Add next tweet from same user if exists
            if index > 0:
                time, tweet_id = self.tweets[u][index - 1]
                heapq.heappush(heap, (-time, tweet_id, u, index - 1))
        
        return result
    
    def follow(self, follower_id, followee_id):
        """Follow a user."""
        if follower_id != followee_id:
            self.following[follower_id].add(followee_id)
    
    def unfollow(self, follower_id, followee_id):
        """Unfollow a user."""
        self.following[follower_id].discard(followee_id)

# ============================================================================
# TEST FUNCTIONS
# ============================================================================
def test_map_problems():
    """Test all hash map problems with examples."""
    
    print("=== MAP (HASH MAP) PROBLEMS & SOLUTIONS ===\n")
    
    # Test 1: Group Anagrams
    print("1. GROUP ANAGRAMS")
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: {strs1}")
    print(f"Groups: {group_anagrams(strs1)}")
    
    # Test 2: Valid Anagram
    print("\n2. VALID ANAGRAM")
    test_pairs = [("anagram", "nagaram"), ("rat", "car")]
    for s, t in test_pairs:
        print(f"'{s}' and '{t}' → {is_anagram(s, t)}")
    
    # Test 3: Top K Frequent Elements
    print("\n3. TOP K FREQUENT ELEMENTS")
    nums3 = [1, 1, 1, 2, 2, 3]
    k3 = 2
    print(f"Array: {nums3}, k: {k3}")
    print(f"Top {k3} frequent: {top_k_frequent(nums3, k3)}")
    
    # Test 4: Longest Substring Without Repeating Characters
    print("\n4. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS")
    test_strings = ["abcabcbb", "bbbbb", "pwwkew"]
    for s in test_strings:
        print(f"'{s}' → length {length_of_longest_substring(s)}")
    
    # Test 5: Find All Anagrams
    print("\n5. FIND ALL ANAGRAMS IN A STRING")
    s5, p5 = "abab", "ab"
    print(f"String: '{s5}', Pattern: '{p5}'")
    print(f"Anagram indices: {find_anagrams(s5, p5)}")
    
    # Test 6: Word Pattern
    print("\n6. WORD PATTERN")
    pattern6 = "abba"
    s6 = "dog cat cat dog"
    print(f"Pattern: '{pattern6}', String: '{s6}'")
    print(f"Follows pattern: {word_pattern(pattern6, s6)}")
    
    # Test 7: Isomorphic Strings
    print("\n7. ISOMORPHIC STRINGS")
    test_iso = [("egg", "add"), ("foo", "bar")]
    for s, t in test_iso:
        print(f"'{s}' and '{t}' → {is_isomorphic(s, t)}")
    
    # Test 8: Minimum Window Substring
    print("\n8. MINIMUM WINDOW SUBSTRING")
    s8, t8 = "ADOBECODEBANC", "ABC"
    print(f"String: '{s8}', Target: '{t8}'")
    print(f"Minimum window: '{min_window(s8, t8)}'")
    
    # Test 9: First Unique Character
    print("\n9. FIRST UNIQUE CHARACTER")
    s9 = "leetcode"
    print(f"String: '{s9}'")
    print(f"First unique index: {first_uniq_char(s9)}")
    
    # Test 10: Longest Consecutive Sequence
    print("\n10. LONGEST CONSECUTIVE SEQUENCE")
    nums10 = [100, 4, 200, 1, 3, 2]
    print(f"Array: {nums10}")
    print(f"Longest consecutive length: {longest_consecutive(nums10)}")
    
    # Test 11: LRU Cache
    print("\n11. LRU CACHE")
    lru = LRUCache(2)
    operations = [
        ("put", 1, 1), ("put", 2, 2), ("get", 1),
        ("put", 3, 3), ("get", 2), ("get", 3), ("get", 1)
    ]
    for op in operations:
        if op[0] == "put":
            lru.put(op[1], op[2])
            print(f"Put ({op[1]}, {op[2]})")
        else:
            result = lru.get(op[1])
            print(f"Get {op[1]} → {result}")

if __name__ == "__main__":
    test_map_problems()