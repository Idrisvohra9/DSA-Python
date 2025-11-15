"""
Python Array Slicing Practice Problems
=====================================

Solve these problems to master array slicing and splicing!
"""


def problem_1():
    """
    Problem 1: Extract Elements
    Given: arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    Tasks:
    a) Get elements from index 2 to 6 (inclusive of 2, exclusive of 7)
    b) Get the last 4 elements
    c) Get every 3rd element starting from index 1
    d) Get elements from index 3 to 8 in reverse order
    """
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("Problem 1: Extract Elements")
    print(f"Array: {arr}")
    print()

    # Your solutions here:
    print("Solutions")
    print("a) ", arr[2:7])
    print("b) ", arr[-4:])
    print("c) ", arr[1::3])
    print("d) ", arr[3:8][::-1])

    print("Expected answers:")
    print("a) [30, 40, 50, 60, 70]")
    print("b) [70, 80, 90, 100]")
    print("c) [20, 50, 80]")
    print("d) [80, 70, 60, 50, 40]")
    print("-" * 50)


def problem_2():
    """
    Problem 2: String Manipulation
    Given: text = "Programming"

    Tasks:
    a) Extract "gram" from the string
    b) Get every 2nd character starting from the first
    c) Reverse the string
    d) Get the middle 3 characters
    """
    text = "Programming"
    print("Problem 2: String Manipulation")
    print(f"String: '{text}'")
    print()

    # Your solutions here:
    print("a) ", text[3:7])
    print("b) ", text[::2])
    print("c) ", text[::-1])

    print("d) ", text[(len(text) // 2) - 1 : (len(text) // 2) + 2])

    print("Expected answers:")
    print("a) 'gram'")
    print("b) 'Pormig'")
    print("c) 'gnimmargorP'")
    print("d) 'ram'")
    print("-" * 50)


def problem_3():
    """
    Problem 3: Array Modification
    Given: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Tasks:
    a) Replace elements at indices 2-4 with [99, 88, 77]
    b) Insert [0, 0] at index 3 (without replacing existing elements)
    c) Delete elements from index 5 to 7
    d) Replace every other element starting from index 1 with [100, 200, 300, 400, 500]
    """
    print("Problem 3: Array Modification")

    # Task a
    numbers_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original: {numbers_a}")
    # Your solution for a:
    print(f"After task a: {numbers_a}")

    # Task b
    numbers_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original: {numbers_b}")
    # Your solution for b:
    print(f"After task b: {numbers_b}")

    # Task c
    numbers_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original: {numbers_c}")
    # Your solution for c:
    print(f"After task c: {numbers_c}")

    # Task d
    numbers_d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original: {numbers_d}")
    # Your solution for d:
    print(f"After task d: {numbers_d}")

    print("Expected answers:")
    print("a) [1, 2, 99, 88, 77, 6, 7, 8, 9, 10]")
    print("b) [1, 2, 3, 0, 0, 4, 5, 6, 7, 8, 9, 10]")
    print("c) [1, 2, 3, 4, 5, 9, 10]")
    print("d) [1, 100, 3, 200, 5, 300, 7, 400, 9, 500]")
    print("-" * 50)


def problem_4():
    """
    Problem 4: Implement Functions
    Implement these functions using array slicing:
    """

    def get_first_n(arr, n):
        """Return the first n elements of the array"""
        return arr[:n]

    def get_last_n(arr, n):
        """Return the last n elements of the array"""
        return arr[-n:]

    def remove_first_n(arr, n):
        """Return array with first n elements removed"""
        return arr[n:]

    def remove_last_n(arr, n):
        """Return array with last n elements removed"""
        return arr[:-n]

    def reverse_array(arr):
        """Return reversed array using slicing"""
        return arr[::-1]

    def get_every_nth(arr, n):
        """Return every nth element from the array"""
        return arr[::n]

    def split_array_half(arr):
        """Split array into two halves and return both"""
        mid = len(arr) // 2
        return [arr[:mid], arr[mid:]]

    # Test your functions
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Problem 4: Function Implementation")
    print(f"Test array: {test_arr}")
    print()

    # Uncomment to test your functions:
    print(f"First 3: {get_first_n(test_arr, 3)}")
    print(f"Last 4: {get_last_n(test_arr, 4)}")
    print(f"Remove first 2: {remove_first_n(test_arr, 2)}")
    print(f"Remove last 3: {remove_last_n(test_arr, 3)}")
    print(f"Reversed: {reverse_array(test_arr)}")
    print(f"Every 3rd: {get_every_nth(test_arr, 3)}")
    print(f"Split in half: {split_array_half(test_arr)}")

    print("Expected outputs:")
    print("First 3: [1, 2, 3]")
    print("Last 4: [7, 8, 9, 10]")
    print("Remove first 2: [3, 4, 5, 6, 7, 8, 9, 10]")
    print("Remove last 3: [1, 2, 3, 4, 5, 6, 7]")
    print("Reversed: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]")
    print("Every 3rd: [1, 4, 7, 10]")
    print("Split in half: ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])")
    print("-" * 50)


def problem_5():
    """
    Problem 5: Advanced Challenges
    """

    def rotate_right(arr, k):
        """Rotate array to the right by k positions using slicing"""
        k = k % len(arr)
        return arr[-k:] + arr[:-k]

    def rotate_left(arr, k):
        """Rotate array to the left by k positions using slicing"""
        k = k % len(arr)
        return arr[k:] + arr[:k]

    def palindrome_check(s):
        """Check if string is palindrome using slicing"""
        return s[::-1] == s

    def extract_alternating(arr, start_index=0):
        """Extract alternating elements starting from start_index"""
        return arr[start_index::2]

    def insert_at_middle(arr, elements):
        """Insert elements at the middle of the array"""
        mid = len(arr) // 2
        arr[mid:mid] = elements
        return arr

    # Test cases
    print("Problem 5: Advanced Challenges")
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Test array: {test_arr}")

    # Uncomment to test:
    print(f"Rotate right by 3: {rotate_right(test_arr, 3)}")
    print(f"Rotate left by 2: {rotate_left(test_arr, 2)}")
    print(f"'racecar' is palindrome: {palindrome_check('racecar')}")
    print(f"'hello' is palindrome: {palindrome_check('hello')}")
    print(f"Alternating from index 0: {extract_alternating(test_arr, 0)}")
    print(f"Alternating from index 1: {extract_alternating(test_arr, 1)}")
    print(f"Insert [99, 100] at middle: {insert_at_middle(test_arr, [99, 100])}")

    print("Expected outputs:")
    print("Rotate right by 3: [6, 7, 8, 1, 2, 3, 4, 5]")
    print("Rotate left by 2: [3, 4, 5, 6, 7, 8, 1, 2]")
    print("'racecar' is palindrome: True")
    print("'hello' is palindrome: False")
    print("Alternating from index 0: [1, 3, 5, 7]")
    print("Alternating from index 1: [2, 4, 6, 8]")
    print("Insert [99, 100] at middle: [1, 2, 3, 4, 99, 100, 5, 6, 7, 8]")
    print("-" * 50)


def problem_6():
    """
    Problem 6: Real-world Applications
    """

    def sliding_window_max(arr, window_size):
        """Find maximum in each sliding window of given size"""
        # Use slicing to create windows and find max of each
        max_arr = []
        n = 0
        for _ in range(len(arr)):
            part = arr[n : window_size + n]
            if len(part) == window_size:
                max_arr.append(max(part))
            n += 1
        return max_arr

    def remove_vowels_at_positions(text, positions):
        """Remove characters at given positions using slicing"""
        vowels = ["a", "e", "i", "o", "u"]
        text_arr = list(text)
        for pos in positions:
            if not pos > len(text_arr):
                if text_arr[pos] in vowels:
                    text_arr[pos : pos + 1] = []
        return "".join(text_arr)

    def chunk_array(arr, chunk_size):
        """Split array into chunks of given size"""
        output = []
        skip_size = 0
        for _ in range(len(arr)):
            if skip_size <= len(arr):
                output.append(arr[skip_size : chunk_size + skip_size])
                skip_size += chunk_size
        return output

    def merge_alternating(arr1, arr2):
        """Merge two arrays by alternating elements"""
        output = []
        smaller = min(len(arr1), len(arr2))
        for i in range(smaller):
            output.append(arr1[i])
            output.append(arr2[i])
            
        if len(arr1) > len(arr2):
            output.extend(arr1[smaller:])
        elif len(arr2) > len(arr1):
            output.extend(arr2[smaller:])
        return output

    # Test cases
    print("Problem 6: Real-world Applications")

    # Uncomment to test:
    print(
        f"Sliding window max [1,3,2,5,4,7,6] size 3: {sliding_window_max([1,3,2,5,4,7,6], 3)}"
    )
    print(
        f"Remove positions [1,3,5] from 'hello': {remove_vowels_at_positions('hello', [1,3,5])}"
    )
    print(f"Chunk [1,2,3,4,5,6,7,8] size 3: {chunk_array([1,2,3,4,5,6,7,8], 3)}")
    print(f"Merge [1,3,5] and [2,4,6]: {merge_alternating([1,3,5], [2,4,6])}")

    print("Expected outputs:")
    print("Sliding window max [1,3,2,5,4,7,6] size 3: [3, 5, 5, 7, 7]")
    print("Remove positions [1,3,5] from 'hello': 'hlo'")
    print("Chunk [1,2,3,4,5,6,7,8] size 3: [[1, 2, 3], [4, 5, 6], [7, 8]]")
    print("Merge [1,3,5] and [2,4,6]: [1, 2, 3, 4, 5, 6]")
    print("-" * 50)


if __name__ == "__main__":
    print("ARRAY SLICING PRACTICE PROBLEMS")
    print("=" * 50)
    print("Complete each problem by filling in the missing code.")
    print("Run the file to see expected outputs and check your solutions.")
    print("=" * 50)
    print()

    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()
    problem_6()

    print("\nTIPS FOR SUCCESS:")
    print("1. Remember: list[start:stop:step]")
    print("2. Negative indices count from the end")
    print("3. Slicing creates a new list/string")
    print("4. Empty slice [] can delete elements")
    print("5. Practice with different step values")
    print("6. Test edge cases (empty arrays, single elements)")
