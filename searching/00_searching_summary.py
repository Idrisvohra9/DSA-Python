"""
SEARCHING ALGORITHMS - COMPREHENSIVE SUMMARY
==========================================
This file provides a complete overview of all implemented searching algorithms,
their characteristics, use cases, and when to choose each one.

All algorithms work on SORTED arrays unless otherwise specified.
"""

# Import all search algorithms for comparison
# Note: These imports work when running from the parent directory
# For standalone execution, the functions are re-implemented below

def linear_search(arr, target):
    """Basic linear search implementation for demonstration."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """Basic binary search implementation for demonstration."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def jump_search(arr, target):
    """Basic jump search implementation for demonstration."""
    import math
    n = len(arr)
    if n == 0:
        return -1
    
    jump_size = int(math.sqrt(n))
    prev = 0
    
    while arr[min(jump_size, n) - 1] < target:
        prev = jump_size
        jump_size += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    while arr[prev] < target:
        prev += 1
        if prev == min(jump_size, n):
            return -1
    
    return prev if arr[prev] == target else -1

def interpolation_search(arr, target):
    """Basic interpolation search implementation for demonstration."""
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        if left == right:
            return left if arr[left] == target else -1
        
        pos = left + int(((target - arr[left]) / (arr[right] - arr[left])) * (right - left))
        pos = max(left, min(pos, right))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] > target:
            right = pos - 1
        else:
            left = pos + 1
    
    return -1

def exponential_search(arr, target):
    """Basic exponential search implementation for demonstration."""
    if len(arr) == 0:
        return -1
    if arr[0] == target:
        return 0
    
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2
    
    # Binary search in range
    left = bound // 2
    right = min(bound, len(arr) - 1)
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def ternary_search(arr, target):
    """Basic ternary search implementation for demonstration."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

def fibonacci_search(arr, target):
    """Basic fibonacci search implementation for demonstration."""
    n = len(arr)
    if n == 0:
        return -1
    
    fib_m2, fib_m1 = 0, 1
    fib_m = fib_m2 + fib_m1
    
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    offset = -1
    
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i
    
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1

def algorithm_comparison_table():
    """
    Display a comprehensive comparison table of all searching algorithms.
    """
    print("SEARCHING ALGORITHMS COMPARISON TABLE")
    print("=" * 80)
    
    algorithms = [
        {
            'name': 'Linear Search',
            'time_best': 'O(1)',
            'time_avg': 'O(n)',
            'time_worst': 'O(n)',
            'space': 'O(1)',
            'sorted_required': 'No',
            'best_for': 'Small/unsorted arrays'
        },
        {
            'name': 'Binary Search',
            'time_best': 'O(1)',
            'time_avg': 'O(log n)',
            'time_worst': 'O(log n)',
            'space': 'O(1)',
            'sorted_required': 'Yes',
            'best_for': 'General purpose, sorted arrays'
        },
        {
            'name': 'Jump Search',
            'time_best': 'O(1)',
            'time_avg': 'O(√n)',
            'time_worst': 'O(√n)',
            'space': 'O(1)',
            'sorted_required': 'Yes',
            'best_for': 'When binary search jumps are expensive'
        },
        {
            'name': 'Interpolation Search',
            'time_best': 'O(1)',
            'time_avg': 'O(log log n)',
            'time_worst': 'O(n)',
            'space': 'O(1)',
            'sorted_required': 'Yes (uniform)',
            'best_for': 'Uniformly distributed sorted arrays'
        },
        {
            'name': 'Exponential Search',
            'time_best': 'O(1)',
            'time_avg': 'O(log n)',
            'time_worst': 'O(log n)',
            'space': 'O(1)',
            'sorted_required': 'Yes',
            'best_for': 'Unbounded/infinite arrays'
        },
        {
            'name': 'Ternary Search',
            'time_best': 'O(1)',
            'time_avg': 'O(log₃ n)',
            'time_worst': 'O(log₃ n)',
            'space': 'O(1)',
            'sorted_required': 'Yes',
            'best_for': 'When iterations are expensive'
        },
        {
            'name': 'Fibonacci Search',
            'time_best': 'O(1)',
            'time_avg': 'O(log n)',
            'time_worst': 'O(log n)',
            'space': 'O(1)',
            'sorted_required': 'Yes',
            'best_for': 'When division is expensive'
        }
    ]
    
    # Print header
    print(f"{'Algorithm':<20} {'Best':<12} {'Average':<15} {'Worst':<12} {'Space':<8} {'Sorted?':<12} {'Best For'}")
    print("-" * 120)
    
    # Print each algorithm
    for alg in algorithms:
        print(f"{alg['name']:<20} {alg['time_best']:<12} {alg['time_avg']:<15} {alg['time_worst']:<12} "
              f"{alg['space']:<8} {alg['sorted_required']:<12} {alg['best_for']}")


def performance_comparison(sizes=[10, 100, 1000, 10000]):
    """
    Compare theoretical performance of different algorithms for various array sizes.
    """
    import math
    
    print("\nPERFORMANCE COMPARISON FOR DIFFERENT ARRAY SIZES")
    print("=" * 60)
    
    print(f"{'Size':<8} {'Linear':<8} {'Binary':<8} {'Jump':<8} {'Ternary':<8} {'Notes'}")
    print("-" * 60)
    
    for n in sizes:
        linear = n                                    # O(n)
        binary = math.ceil(math.log2(n))             # O(log₂ n)
        jump = math.ceil(math.sqrt(n))               # O(√n)
        ternary = math.ceil(math.log(n) / math.log(3))  # O(log₃ n)
        
        print(f"{n:<8} {linear:<8} {binary:<8} {jump:<8} {ternary:<8} ", end="")
        
        # Add notes for interesting cases
        if n == 10:
            print("Small arrays - differences minimal")
        elif n == 100:
            print("Jump search starts showing benefits")
        elif n == 1000:
            print("Clear advantages for logarithmic algorithms")
        elif n == 10000:
            print("Linear search becomes impractical")


def choose_algorithm_guide():
    """
    Provide guidance on when to choose each searching algorithm.
    """
    print("\nALGORITHM SELECTION GUIDE")
    print("=" * 40)
    
    scenarios = [
        {
            'scenario': 'Small array (< 50 elements)',
            'recommendation': 'Linear Search',
            'reason': 'Simple, no preprocessing needed, overhead of other algorithms not worth it'
        },
        {
            'scenario': 'Unsorted array',
            'recommendation': 'Linear Search',
            'reason': 'Only option without sorting first'
        },
        {
            'scenario': 'General sorted array',
            'recommendation': 'Binary Search',
            'reason': 'Best general-purpose algorithm, widely understood, efficient'
        },
        {
            'scenario': 'Very large sorted array',
            'recommendation': 'Binary Search',
            'reason': 'Consistently O(log n) performance regardless of data distribution'
        },
        {
            'scenario': 'Uniformly distributed data',
            'recommendation': 'Interpolation Search',
            'reason': 'Can achieve O(log log n) performance with uniform distribution'
        },
        {
            'scenario': 'Unknown/infinite array size',
            'recommendation': 'Exponential Search',
            'reason': 'Finds range first, then binary search within range'
        },
        {
            'scenario': 'Expensive random access',
            'recommendation': 'Jump Search',
            'reason': 'Reduces number of random accesses compared to binary search'
        },
        {
            'scenario': 'Expensive division operations',
            'recommendation': 'Fibonacci Search',
            'reason': 'Only uses addition and subtraction, no division needed'
        },
        {
            'scenario': 'Many searches on same array',
            'recommendation': 'Binary Search',
            'reason': 'Consistent performance, well-optimized in most systems'
        },
        {
            'scenario': 'Embedded systems with limited resources',
            'recommendation': 'Binary/Fibonacci Search',
            'reason': 'Low memory overhead, predictable performance'
        }
    ]
    
    for i, item in enumerate(scenarios, 1):
        print(f"\n{i}. {item['scenario']}")
        print(f"   → {item['recommendation']}")
        print(f"   Reason: {item['reason']}")


def algorithm_characteristics():
    """
    Detailed characteristics of each algorithm.
    """
    print("\nDETAILED ALGORITHM CHARACTERISTICS")
    print("=" * 45)
    
    characteristics = {
        'Linear Search': {
            'pros': [
                'Works on unsorted arrays',
                'Simple implementation',
                'No preprocessing required',
                'Good for small arrays',
                'Stable (finds first occurrence)'
            ],
            'cons': [
                'O(n) time complexity',
                'Inefficient for large arrays',
                'No early termination optimizations'
            ],
            'variants': [
                'Sentinel Linear Search',
                'Binary Linear Search',
                'Recursive Linear Search'
            ]
        },
        
        'Binary Search': {
            'pros': [
                'O(log n) time complexity',
                'Very efficient for large arrays',
                'Well-understood and optimized',
                'Predictable performance'
            ],
            'cons': [
                'Requires sorted array',
                'Random access needed',
                'Not cache-friendly for very large arrays'
            ],
            'variants': [
                'Recursive Binary Search',
                'Iterative Binary Search',
                'Binary Search on Answer'
            ]
        },
        
        'Jump Search': {
            'pros': [
                'Better than linear for large arrays',
                'Fewer comparisons than linear',
                'Good when binary search jumps are expensive'
            ],
            'cons': [
                'Still O(√n), worse than binary',
                'Requires sorted array',
                'Need to determine optimal jump size'
            ],
            'variants': [
                'Variable Jump Search',
                'Adaptive Jump Search'
            ]
        },
        
        'Interpolation Search': {
            'pros': [
                'O(log log n) for uniform data',
                'Very fast for appropriate data',
                'Intuitive position estimation'
            ],
            'cons': [
                'O(n) worst case',
                'Requires uniform distribution',
                'Complex position calculation'
            ],
            'variants': [
                'Adaptive Interpolation Search',
                'Quadratic Interpolation Search'
            ]
        },
        
        'Exponential Search': {
            'pros': [
                'Works with unbounded arrays',
                'O(log n) like binary search',
                'Good when target is near beginning'
            ],
            'cons': [
                'Two-phase algorithm',
                'Requires sorted array',
                'Extra overhead for bound finding'
            ],
            'variants': [
                'Doubling Search',
                'Galloping Search'
            ]
        },
        
        'Ternary Search': {
            'pros': [
                'Fewer iterations than binary',
                'Good for expensive iteration setup',
                'Useful for finding extrema'
            ],
            'cons': [
                'More comparisons per iteration',
                'Generally slower than binary',
                'More complex implementation'
            ],
            'variants': [
                'Recursive Ternary Search',
                'Ternary Search for Functions'
            ]
        },
        
        'Fibonacci Search': {
            'pros': [
                'No division operations',
                'O(log n) performance',
                'Good for systems with expensive division'
            ],
            'cons': [
                'Complex implementation',
                'Requires Fibonacci number generation',
                'Not commonly used in practice'
            ],
            'variants': [
                'Golden Section Search',
                'Modified Fibonacci Search'
            ]
        }
    }
    
    for alg_name, details in characteristics.items():
        print(f"\n{alg_name.upper()}")
        print("-" * len(alg_name))
        
        print("Pros:")
        for pro in details['pros']:
            print(f"  + {pro}")
        
        print("Cons:")
        for con in details['cons']:
            print(f"  - {con}")
        
        print("Variants:")
        for variant in details['variants']:
            print(f"  • {variant}")


def practical_examples():
    """
    Real-world examples of when to use each algorithm.
    """
    print("\nPRACTICAL EXAMPLES AND USE CASES")
    print("=" * 40)
    
    examples = [
        {
            'algorithm': 'Linear Search',
            'examples': [
                'Finding a name in an unsorted contact list',
                'Searching for a file in a directory',
                'Looking for an item in a shopping cart',
                'Finding a specific log entry by content'
            ]
        },
        {
            'algorithm': 'Binary Search',
            'examples': [
                'Looking up a word in a dictionary',
                'Finding a record in a sorted database index',
                'Searching version control history',
                'Finding a value in a sorted configuration file'
            ]
        },
        {
            'algorithm': 'Jump Search',
            'examples': [
                'Searching large sorted files on slow storage',
                'Finding records in tape storage systems',
                'Searching in memory-mapped large files',
                'Database range queries with expensive seeks'
            ]
        },
        {
            'algorithm': 'Interpolation Search',
            'examples': [
                'Searching phone book by name (alphabetically uniform)',
                'Finding data in scientific measurements (uniform intervals)',
                'Searching employee records by ID (sequential IDs)',
                'Finding time-series data with regular intervals'
            ]
        },
        {
            'algorithm': 'Exponential Search',
            'examples': [
                'Searching infinite data streams',
                'Finding elements in dynamic arrays',
                'Searching in very large arrays where size is unknown',
                'Looking through log files of unknown length'
            ]
        },
        {
            'algorithm': 'Ternary Search',
            'examples': [
                'Finding maximum/minimum in unimodal functions',
                'Optimization problems in mathematics',
                'Finding peaks in signal processing',
                'Game AI for finding optimal moves'
            ]
        },
        {
            'algorithm': 'Fibonacci Search',
            'examples': [
                'Embedded systems with limited arithmetic units',
                'Ancient computers without fast division',
                'Specialized hardware with only add/subtract',
                'Mathematical optimization requiring golden ratio'
            ]
        }
    ]
    
    for example in examples:
        print(f"\n{example['algorithm'].upper()}")
        print("-" * len(example['algorithm']))
        for use_case in example['examples']:
            print(f"  • {use_case}")


def implementation_tips():
    """
    Tips for implementing each searching algorithm effectively.
    """
    print("\nIMPLEMENTATION TIPS AND BEST PRACTICES")
    print("=" * 45)
    
    tips = {
        'General': [
            'Always validate input parameters (array, target)',
            'Handle edge cases (empty array, single element)',
            'Consider integer overflow in index calculations',
            'Add bounds checking to prevent array access errors',
            'Use meaningful variable names for clarity'
        ],
        
        'Binary Search': [
            'Use "left + (right - left) // 2" to avoid overflow',
            'Be careful with inclusive/exclusive bounds',
            'Consider iterative vs recursive based on stack limitations',
            'Handle duplicate elements consistently',
            'Test with arrays of different sizes'
        ],
        
        'Jump Search': [
            'Optimal jump size is √n for general cases',
            'Consider adaptive jump sizes for specific data',
            'Combine with binary search for hybrid approach',
            'Profile different jump sizes for your use case'
        ],
        
        'Interpolation Search': [
            'Verify data is uniformly distributed before using',
            'Add fallback to binary search for non-uniform data',
            'Handle division by zero when all elements are equal',
            'Use integer arithmetic when possible',
            'Consider floating-point precision issues'
        ],
        
        'All Algorithms': [
            'Write comprehensive test cases',
            'Benchmark against your specific data',
            'Consider cache locality for very large arrays',
            'Document time/space complexity',
            'Profile in your target environment'
        ]
    }
    
    for category, tip_list in tips.items():
        print(f"\n{category.upper()}")
        print("-" * len(category))
        for tip in tip_list:
            print(f"  • {tip}")


def demonstrate_all_algorithms():
    """
    Demonstrate all algorithms on the same dataset for comparison.
    """
    print("\nDEMONSTRATING ALL ALGORITHMS ON SAME DATA")
    print("=" * 50)
    
    # Create test data
    test_array = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
    target = 35
    
    print(f"Test Array: {test_array}")
    print(f"Searching for: {target}")
    print(f"Array length: {len(test_array)}")
    print()
    
    # Test each algorithm
    algorithms = [
        ('Linear Search', linear_search),
        ('Binary Search', binary_search),
        ('Jump Search', jump_search),
        ('Interpolation Search', interpolation_search),
        ('Exponential Search', exponential_search),
        ('Ternary Search', ternary_search),
        ('Fibonacci Search', fibonacci_search)
    ]
    
    results = []
    
    for name, func in algorithms:
        try:
            result = func(test_array, target)
            results.append((name, result))
            status = "✅ Found" if result != -1 else "❌ Not found"
            print(f"{name:<20}: Index {result:>2} ({status})")
        except Exception as e:
            print(f"{name:<20}: Error - {e}")
    
    # Verify all results are consistent
    print()
    found_indices = [result for name, result in results if result != -1]
    if found_indices and all(idx == found_indices[0] for idx in found_indices):
        print(f"✅ All algorithms found target at index {found_indices[0]}")
    else:
        print("⚠️  Inconsistent results detected!")


if __name__ == "__main__":
    print("COMPREHENSIVE SEARCHING ALGORITHMS GUIDE")
    print("=" * 50)
    
    # Display all sections
    algorithm_comparison_table()
    performance_comparison()
    choose_algorithm_guide()
    algorithm_characteristics()
    practical_examples()
    implementation_tips()
    demonstrate_all_algorithms()
    
    print("\n" + "=" * 50)
    print("CONCLUSION")
    print("=" * 50)
    print("Choosing the right searching algorithm depends on:")
    print("1. Whether your data is sorted")
    print("2. The size of your dataset")
    print("3. The distribution of your data")
    print("4. How often you'll be searching")
    print("5. Your system's constraints (memory, processing power)")
    print()
    print("For most practical purposes:")
    print("• Use Linear Search for small or unsorted data")
    print("• Use Binary Search for general sorted data")
    print("• Consider specialized algorithms for specific scenarios")
    print()
    print("Remember: Profile and benchmark with your actual data!")