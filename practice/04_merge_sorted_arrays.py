import time


def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into one sorted array using two-pointer technique.
    Time Complexity: O(m+n), Space Complexity: O(m+n)
    """
    merged = []  # result list to collect merged elements
    i = j = 0  # i -> index in arr1, j -> index in arr2
    total = len(arr1) + len(arr2)  # total elements we must append

    # Loop exactly 'total' times so we consume every element from both arrays.
    for _ in range(total):
        # Choose from arr1 when:
        #  - arr1 still has elements (i < len(arr1)), AND
        #  - (arr2 is exhausted) OR (current arr1 element <= current arr2 element)
        # The `<=` tie-breaker favors arr1 when elements are equal (stable with arr1 first).
        if i < len(arr1) and (j >= len(arr2) or arr1[i] <= arr2[j]):
            merged.append(arr1[i])  # append current arr1 item
            i += 1  # advance arr1 pointer
        else:
            merged.append(arr2[j])  # append current arr2 item
            j += 1  # advance arr2 pointer

    return merged  # merged is sorted because both inputs were sorted


def merge_sorted_arrays_simple(arr1, arr2):
    """
    Simple but less efficient approach.
    Time Complexity: O((m+n)log(m+n)), Space Complexity: O(m+n)
    """
    return sorted(arr1 + arr2)


def measure(func, *args, max_repeat_small=10000, max_repeat_large=100):
    """
    Measure execution time of func(*args).
    Chooses a repeat count depending on input size to get stable timings.
    Returns (result, total_time_s, avg_time_s).
    """
    total_len = 0
    for a in args:
        try:
            total_len += len(a)
        except Exception:
            pass

    repeats = max_repeat_small if total_len <= 100 else max_repeat_large

    # Warmup run
    result = func(*args)

    start = time.perf_counter()
    for _ in range(repeats):
        result = func(*args)
    end = time.perf_counter()

    total = end - start
    avg = total / repeats
    print(
        f"{func.__name__}: total={total:.6f}s over {repeats} runs, avg={avg*1e6:.2f} µs"
    )
    return result, total, avg


# Test inputs - Small arrays
print("=== SMALL ARRAYS (9 elements total) ===")
arr1_small = [1, 3, 5, 7]
arr2_small = [2, 4, 6, 8, 9]

print("Optimal solution (Two-pointer):")
opt_result, opt_total, opt_avg = measure(merge_sorted_arrays, arr1_small, arr2_small)
print(f"Merged array: {opt_result}")

print("\nSimple solution (Concatenate + Sort):")
simp_result, simp_total, simp_avg = measure(merge_sorted_arrays_simple, arr1_small, arr2_small)
print(f"Merged array: {simp_result}")

# Test with LARGE arrays to see the difference
print("\n=== LARGE ARRAYS (20,000 elements total) ===")
arr1_large = list(range(0, 20000, 2))  # [0, 2, 4, 6, ..., 19998] - 10,000 elements
arr2_large = list(range(1, 20000, 2))  # [1, 3, 5, 7, ..., 19999] - 10,000 elements

print("Optimal solution (Two-pointer) - Large:")
opt_result_large, opt_total_large, opt_avg_large = measure(merge_sorted_arrays, arr1_large, arr2_large, max_repeat_large=10)
print(f"Result length: {len(opt_result_large)}")

print("\nSimple solution (Concatenate + Sort) - Large:")
simp_result_large, simp_total_large, simp_avg_large = measure(merge_sorted_arrays_simple, arr1_large, arr2_large, max_repeat_large=10)
print(f"Result length: {len(simp_result_large)}")

print(f"\n🚀 SPEED COMPARISON FOR LARGE ARRAYS:")
if opt_avg_large < simp_avg_large:
    speedup = simp_avg_large / opt_avg_large
    print(f"Two-pointer is {speedup:.2f}x FASTER than simple solution!")
else:
    speedup = opt_avg_large / simp_avg_large
    print(f"Simple solution is {speedup:.2f}x faster (unexpected!)")

# Test with edge cases and measure
print("\n=== EDGE CASES ===")
res1, *_ = measure(merge_sorted_arrays, [], [1, 2, 3])
print(f"Empty + [1,2,3]: {res1}")
res2, *_ = measure(merge_sorted_arrays, [1, 2, 3], [])
print(f"[1,2,3] + Empty: {res2}")
res3, *_ = measure(merge_sorted_arrays, [1], [2])
print(f"Single elements: {res3}")
