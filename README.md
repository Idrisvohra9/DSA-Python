# 🚀 Complete Data Structures & Algorithms in Python

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Functions](https://img.shields.io/badge/Functions-200%2B-green.svg)](#total-functions)
[![Topics](https://img.shields.io/badge/Topics-15%2B-orange.svg)](#covered-topics)
[![LeetCode](https://img.shields.io/badge/LeetCode-Ready-brightgreen.svg)](#leetcode-solutions)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **⭐ Star this repository** if you find it helpful for your DSA learning journey!

## 📚 Overview

This repository contains a **comprehensive collection** of Data Structures and Algorithms implemented in Python with detailed explanations, step-by-step visualizations, and educational comments. Perfect for interview preparation, academic learning, and competitive programming.

## 🎯 Why This Repository?

- **🎓 Educational Focus**: Every algorithm has detailed comments explaining how it works
- **📊 Visual Learning**: Step-by-step execution with print statements
- **🧪 Comprehensive Testing**: Each implementation includes multiple test cases
- **⚡ Performance Analysis**: Time and space complexity explanations
- **🎯 Interview Ready**: LeetCode-style problems with optimal solutions
- **🏗️ Production Quality**: Clean, readable, and well-documented code

## 📊 Repository Statistics

### 📈 Total Functions & Classes

- **200+ Functions and Classes** implemented across all topics
- **50+ Python files** with comprehensive implementations
- **15+ Core DSA Topics** covered in depth

### 🎯 Coverage Breakdown

| Category             | Files | Functions | Problems                |
| -------------------- | ----- | --------- | ----------------------- |
| Sorting Algorithms   | 8     | 30+       | All major sorts         |
| Searching Algorithms | 8     | 40+       | From linear to advanced |
| Data Structures      | 13    | 60+       | Fundamental to advanced |
| LeetCode Problems    | 17    | 50+       | Interview favorites     |
| Practice Problems    | 11    | 20+       | Skill builders          |

## 🗂️ Repository Structure

```
📁 DSA-Python/
├── 📁 basics/                    # Fundamental data structures
├── 📁 sorting/                   # Complete sorting algorithms collection
├── 📁 searching/                 # Advanced searching techniques
├── 📁 practice/                  # Skill-building exercises
├── 📁 leetcode_problems/         # Interview-style problems
└── 📄 README.md                  # This comprehensive guide
```

---

## 📚 Covered Topics

### 🔍 1. Searching Algorithms

**Location**: [`/searching/`](./searching/)

Master all essential searching techniques with detailed implementations:

| Algorithm                | File                                                                   | Time Complexity | Best For                           |
| ------------------------ | ---------------------------------------------------------------------- | --------------- | ---------------------------------- |
| **Linear Search**        | [`01_linear_search.py`](./searching/01_linear_search.py)               | O(n)            | Small/unsorted arrays              |
| **Binary Search**        | [`02_binary_search.py`](./searching/02_binary_search.py)               | O(log n)        | Sorted arrays (general)            |
| **Jump Search**          | [`03_jump_search.py`](./searching/03_jump_search.py)                   | O(√n)           | Large arrays with expensive access |
| **Interpolation Search** | [`04_interpolation_search.py`](./searching/04_interpolation_search.py) | O(log log n)    | Uniformly distributed data         |
| **Exponential Search**   | [`05_exponential_search.py`](./searching/05_exponential_search.py)     | O(log n)        | Unbounded/infinite arrays          |
| **Ternary Search**       | [`06_ternary_search.py`](./searching/06_ternary_search.py)             | O(log₃ n)       | Finding extrema                    |
| **Fibonacci Search**     | [`07_fibonacci_search.py`](./searching/07_fibonacci_search.py)         | O(log n)        | Division-expensive systems         |

**🎯 Key Features:**

- Step-by-step execution visualization
- Performance comparisons between algorithms
- Edge case handling (empty arrays, duplicates)
- Real-world use case examples

### 🔄 2. Sorting Algorithms

**Location**: [`/sorting/`](./sorting/)

Complete collection of sorting algorithms with performance analysis:

| Algorithm          | File                                                     | Time Complexity | Space    | Stable |
| ------------------ | -------------------------------------------------------- | --------------- | -------- | ------ |
| **Bubble Sort**    | [`01_bubble_sort.py`](./sorting/01_bubble_sort.py)       | O(n²)           | O(1)     | ✅     |
| **Selection Sort** | [`02_selection_sort.py`](./sorting/02_selection_sort.py) | O(n²)           | O(1)     | ❌     |
| **Insertion Sort** | [`03_insertion_sort.py`](./sorting/03_insertion_sort.py) | O(n²)           | O(1)     | ✅     |
| **Merge Sort**     | [`04_merge_sort.py`](./sorting/04_merge_sort.py)         | O(n log n)      | O(n)     | ✅     |
| **Quick Sort**     | [`05_quick_sort.py`](./sorting/05_quick_sort.py)         | O(n log n)      | O(log n) | ❌     |
| **Heap Sort**      | [`06_heap_sort.py`](./sorting/06_heap_sort.py)           | O(n log n)      | O(1)     | ❌     |
| **Counting Sort**  | [`07_counting_sort.py`](./sorting/07_counting_sort.py)   | O(n + k)        | O(k)     | ✅     |
| **Radix Sort**     | [`08_radix_sort.py`](./sorting/08_radix_sort.py)         | O(d × n)        | O(n + k) | ✅     |

**🎯 Key Features:**

- Multiple implementation variants (iterative, recursive, optimized)
- Detailed complexity analysis
- Visual step-by-step execution
- Best/worst case scenario examples

### 🏗️ 3. Data Structures - Fundamentals

**Location**: [`/basics/`](./basics/)

Essential data structures with comprehensive problem collections:

#### 📊 Arrays

**File**: [`array_problems.py`](./basics/array_problems.py)

- **15 Classic Problems** including Two Sum, Maximum Subarray, Product of Array
- Sliding window techniques
- Two-pointer algorithms
- Dynamic programming on arrays

#### 🔗 Linked Lists

**Files**: [`linked_list.py`](./basics/linked_list.py) | [`linked_list_problems.py`](./basics/linked_list_problems.py)

- **10 Essential Problems** including cycle detection, reversal, merging
- Singly and doubly linked list implementations
- Fast/slow pointer techniques
- Advanced manipulations

#### 📚 Stacks

**Files**: [`stack.py`](./basics/stack.py) | [`stack_problems.py`](./basics/stack_problems.py)

- **12 Stack Problems** including balanced parentheses, next greater element
- Stack-based algorithms
- Expression evaluation
- Monotonic stack patterns

#### 🚌 Queues

**Files**: [`queue.py`](./basics/queue.py) | [`queue_problems.py`](./basics/queue_problems.py)

- **12 Queue Problems** including sliding window maximum, level order traversal
- Circular queue implementation
- Deque applications
- Priority queue patterns

#### 🗺️ Hash Maps

**File**: [`map_problems.py`](./basics/map_problems.py)

- **14 HashMap Problems** including frequency counting, grouping algorithms
- Hash table collision handling
- Optimization techniques
- Real-world applications

### 🌳 4. Tree Data Structures

**Location**: [`/basics/`](./basics/)

#### 🌲 Binary Trees

**File**: [`binary_tree_problems.py`](./basics/binary_tree_problems.py)

- **16 Binary Tree Problems** including traversals, diameter, path sum
- All traversal methods (inorder, preorder, postorder, level-order)
- Tree construction algorithms
- Advanced tree algorithms

#### 🌴 General Trees

**File**: [`tree_problems.py`](./basics/tree_problems.py)

- **12 Tree Problems** including N-ary trees, trie operations
- Tree serialization/deserialization
- Tree comparison algorithms
- Advanced tree manipulations

### 🎯 5. Practice Problems

**Location**: [`/practice/`](./practice/)

Skill-building exercises progressing from basic to advanced:

| Problem                | File                                                                                            | Concept             |
| ---------------------- | ----------------------------------------------------------------------------------------------- | ------------------- |
| Sum of Evens           | [`01_sum_of_evens.py`](./practice/01_sum_of_evens.py)                                           | Basic iteration     |
| Count Occurrences      | [`02_count_occurences.py`](./practice/02_count_occurences.py)                                   | Hash maps           |
| Find Second Largest    | [`03_find_second_largest.py`](./practice/03_find_second_largest.py)                             | Array traversal     |
| Merge Sorted Arrays    | [`04_merge_sorted_arrays.py`](./practice/04_merge_sorted_arrays.py)                             | Two pointers        |
| Valid Parentheses      | [`05_valid_paranthesis.py`](./practice/05_valid_paranthesis.py)                                 | Stack operations    |
| Reverse String (Stack) | [`06_reverse_string_stack.py`](./practice/06_reverse_string_stack.py)                           | Stack manipulation  |
| MinStack               | [`07_min_element_stack.py`](./practice/07_min_element_stack.py)                                 | Stack design        |
| Linked List Length     | [`08_length_linked_list.py`](./practice/08_length_linked_list.py)                               | List traversal      |
| Insert at Beginning    | [`09_insert_node_at_beginning.py`](./practice/09_insert_node_at_beginning.py)                   | List insertion      |
| Delete Nodes           | [`10_delete_all_nodes_with_given_value.py`](./practice/10_delete_all_nodes_with_given_value.py) | List deletion       |
| Remove Spaces          | [`11_remove_space_func.py`](./practice/11_remove_space_func.py)                                 | String manipulation |

### 💼 6. LeetCode Problems

**Location**: [`/leetcode_problems/`](./leetcode_problems/)

Interview-ready solutions to popular LeetCode problems:

#### 🔥 Top Interview Problems

- [`valid_paranthesis_multi_bracket.py`](./leetcode_problems/valid_paranthesis_multi_bracket.py) - Valid Parentheses
- [`median_of_two_sorted_arrays.py`](./leetcode_problems/median_of_two_sorted_arrays.py) - Median of Two Sorted Arrays
- [`delete_nodes_from_linked_list_by_arr_nums.py`](./leetcode_problems/delete_nodes_from_linked_list_by_arr_nums.py) - Delete Nodes from Linked List
- [`rotate_arr_start_to_end.py`](./leetcode_problems/rotate_arr_start_to_end.py) - Rotate Array
- [`second_largest_digit_in_a_string.py`](./leetcode_problems/second_largest_digit_in_a_string.py) - Second Largest Digit
- [`zigzag_conversion.py`](./leetcode_problems/zigzag_conversion.py) - ZigZag Conversion

#### 🎮 Game & Logic Problems

- [`tic_tac_toe.py`](./leetcode_problems/tic_tac_toe.py) - Tic Tac Toe Winner
- [`fizz_buzz.py`](./leetcode_problems/fizz_buzz.py) - FizzBuzz Implementation

#### 🔤 String Processing

- [`string_to_integer.py`](./leetcode_problems/string_to_integer.py) - String to Integer (atoi)
- [`valid_parentheses_string_star.py`](./leetcode_problems/valid_parentheses_string_star.py) - Valid Parentheses with Wildcards
- [`numeric_finder.py`](./leetcode_problems/numeric_finder.py) - Numeric Pattern Finding

---

## 🌟 Key Features

### 🎓 Educational Excellence

- **Detailed Comments**: Every line explained for learning
- **Step-by-Step Execution**: Visual algorithm progression
- **Multiple Approaches**: Different solutions for same problem
- **Complexity Analysis**: Time and space complexity for each solution

### 🧪 Comprehensive Testing

- **Edge Cases**: Empty inputs, single elements, large datasets
- **Performance Testing**: Benchmark comparisons
- **Visual Demonstrations**: Print-based algorithm visualization
- **Real Data Examples**: Practical use case scenarios

### 🏗️ Production Quality

- **Clean Code**: PEP 8 compliant, readable structure
- **Type Hints**: Modern Python with type annotations
- **Error Handling**: Robust input validation
- **Documentation**: Comprehensive docstrings

### 📊 Performance Focus

- **Algorithm Comparison**: Side-by-side performance analysis
- **Optimization Techniques**: Multiple implementation variants
- **Memory Efficiency**: Space-optimized solutions
- **Scalability**: Solutions tested with large datasets

---

## 🚀 Getting Started

### 📋 Prerequisites

```bash
Python 3.13+ (recommended)
No external dependencies required!
```

### 💻 Quick Start

```bash
# Clone the repository
git clone https://github.com/Idrisvohra9/DSA-Python.git

# Navigate to the project
cd DSA-Python

# Run any algorithm (example: binary search)
python searching/02_binary_search.py

# Run practice problems
python practice/01_sum_of_evens.py

# Test sorting algorithms
python sorting/04_merge_sort.py
```

### 🧪 Running Examples

Each file is self-contained with comprehensive examples:

```python
# Example: Running binary search with detailed steps
python searching/02_binary_search.py

# Output:
# === BINARY SEARCH DEMONSTRATIONS ===
# 1. BASIC BINARY SEARCH
# Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Searching for: 7
# Found at index: 3
# ...
```

---

## 📖 Study Guide

### 🎯 For Beginners

1. Start with **Practice Problems** [`/practice/`](./practice/)
2. Learn basic **Data Structures** [`/basics/`](./basics/)
3. Master **Sorting Algorithms** [`/sorting/`](./sorting/)

### 🔥 For Interview Prep

1. Focus on **LeetCode Problems** [`/leetcode_problems/`](./leetcode_problems/)
2. Master **Searching Algorithms** [`/searching/`](./searching/)
3. Practice **Advanced Tree Problems** [`/basics/binary_tree_problems.py`](./basics/binary_tree_problems.py)

### 🏆 For Competitive Programming

1. Study all **Algorithm Optimizations**
2. Master **Advanced Data Structures**
3. Focus on **Time/Space Complexity** analysis

---

## 📊 Algorithm Complexity Quick Reference

### Searching Algorithms

| Algorithm     | Best | Average      | Worst    | Space |
| ------------- | ---- | ------------ | -------- | ----- |
| Linear        | O(1) | O(n)         | O(n)     | O(1)  |
| Binary        | O(1) | O(log n)     | O(log n) | O(1)  |
| Jump          | O(1) | O(√n)        | O(√n)    | O(1)  |
| Interpolation | O(1) | O(log log n) | O(n)     | O(1)  |

### Sorting Algorithms

| Algorithm | Best       | Average    | Worst      | Space    | Stable |
| --------- | ---------- | ---------- | ---------- | -------- | ------ |
| Bubble    | O(n)       | O(n²)      | O(n²)      | O(1)     | ✅     |
| Quick     | O(n log n) | O(n log n) | O(n²)      | O(log n) | ❌     |
| Merge     | O(n log n) | O(n log n) | O(n log n) | O(n)     | ✅     |
| Heap      | O(n log n) | O(n log n) | O(n log n) | O(1)     | ❌     |

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🐛 Bug Reports**: Found an issue? Create an issue with details
2. **✨ New Algorithms**: Add more algorithms with proper documentation
3. **📝 Documentation**: Improve comments and explanations
4. **🧪 Test Cases**: Add more comprehensive test scenarios
5. **🎨 Code Style**: Enhance code readability and structure

### 📝 Contribution Guidelines

- Follow existing code style and documentation patterns
- Include comprehensive test cases
- Add detailed comments explaining the algorithm
- Update this README if adding new sections

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Python Community** for excellent language design
- **LeetCode** for inspiring problem-solving approaches
- **Computer Science Education** for algorithm foundations
- **Open Source Community** for collaborative learning

---

## ⭐ Star This Repository!

If this repository helped you in your DSA learning journey, please consider:

1. **⭐ Starring** this repository
2. **🍴 Forking** it for your own use
3. **📤 Sharing** it with fellow developers
4. **🐛 Contributing** improvements back

**Your support motivates continued development and helps others discover this resource!**

---

## 📞 Connect & Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/Idrisvohra9/DSA-Python/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Idrisvohra9/DSA-Python/discussions)
- 📧 **Contact**: Feel free to reach out for questions or suggestions

---

<div align="center">

### 🎯 **Happy Coding & Algorithm Learning!** 🎯

**⭐ Don't forget to star this repository! ⭐**

</div>
