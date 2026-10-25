"""
Sorting Algorithms in Python (All 5 Classic Sorting Algorithms)
==============================================================

This module implements the 5 fundamental sorting algorithms with optimal solutions,
detailed explanations, time and space complexity analyses, and test drivers.

Algorithms Covered:
1. Selection Sort
2. Bubble Sort (Optimized)
3. Insertion Sort (Optimized)
4. Merge Sort (Divide & Conquer)
5. Quick Sort (In-place Partitioning with Median-of-Three)

Summary Comparison Table:
+----------------+----------------+----------------+----------------+-------------------+-----------+----------+
| Algorithm      | Best Case      | Average Case   | Worst Case     | Space Complexity  | Stability | In-Place |
+----------------+----------------+----------------+----------------+-------------------+-----------+----------+
| Selection Sort | O(N^2)         | O(N^2)         | O(N^2)         | O(1)              | No        | Yes      |
| Bubble Sort    | O(N)           | O(N^2)         | O(N^2)         | O(1)              | Yes       | Yes      |
| Insertion Sort | O(N)           | O(N^2)         | O(N^2)         | O(1)              | Yes       | Yes      |
| Merge Sort     | O(N log N)     | O(N log N)     | O(N log N)     | O(N)              | Yes       | No       |
| Quick Sort     | O(N log N)     | O(N log N)     | O(N^2)*        | O(log N) stack    | No        | Yes      |
+----------------+----------------+----------------+----------------+-------------------+-----------+----------+
* Quick Sort worst-case is O(N^2), mitigated to expected O(N log N) using median-of-three/random pivot.
"""

# =====================================================================
# 1. Selection Sort
# =====================================================================
def selection_sort(arr):
    """
    Selection Sort Algorithm:
    Iteratively finds the minimum element from the unsorted portion of the array
    and swaps it into its correct sorted position at the beginning.

    Characteristics:
    - Time Complexity: Best O(N^2), Average O(N^2), Worst O(N^2)
    - Space Complexity: O(1) auxiliary (In-place)
    - Stability: Not stable in standard swap implementation
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# =====================================================================
# 2. Bubble Sort (Optimized with early termination flag)
# =====================================================================
def bubble_sort(arr):
    """
    Bubble Sort Algorithm (Optimized):
    Repeatedly steps through the list, compares adjacent elements, and swaps
    them if they are in the wrong order. Larger elements "bubble up" to the end.

    Optimization:
    - Uses a `swapped` boolean flag. If no two adjacent elements are swapped
      during a complete pass, the list is already fully sorted, so we break early.

    Characteristics:
    - Time Complexity: Best O(N) [already sorted], Average O(N^2), Worst O(N^2)
    - Space Complexity: O(1) auxiliary (In-place)
    - Stability: Stable (preserves relative order of equal elements)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred in this pass, array is already sorted
        if not swapped:
            break
    return arr


# =====================================================================
# 3. Insertion Sort (Optimized with element shifting)
# =====================================================================
def insertion_sort(arr):
    """
    Insertion Sort Algorithm (Optimized):
    Builds the sorted array one item at a time. It takes each element from the
    unsorted portion and inserts it into its correct position among preceding
    sorted elements.

    Optimization:
    - Shifts elements to the right instead of performing expensive swaps,
      stopping as soon as the correct position is found.

    Characteristics:
    - Time Complexity: Best O(N) [already sorted], Average O(N^2), Worst O(N^2)
    - Space Complexity: O(1) auxiliary (In-place)
    - Stability: Stable
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Shift elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# =====================================================================
# 4. Merge Sort (Optimal Divide and Conquer)
# =====================================================================
def merge_sort(arr):
    """
    Merge Sort Algorithm (Recursive Divide and Conquer):
    1. Divide: Split the array into two halves at the midpoint.
    2. Conquer: Recursively sort each half until subarrays of length <= 1 are reached.
    3. Combine: Merge the two sorted halves into a single sorted array.

    Characteristics:
    - Time Complexity: Best O(N log N), Average O(N log N), Worst O(N log N)
    - Space Complexity: O(N) auxiliary space for temporary merge buffers
    - Stability: Stable
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    """Helper function to merge two sorted lists in O(len(left) + len(right))."""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort_in_place(arr, low=0, high=None):
    """
    In-place index-based Merge Sort variant:
    Sorts `arr` directly using indices without returning new list references.
    """
    if high is None:
        high = len(arr) - 1
    if low < high:
        mid = (low + high) // 2
        merge_sort_in_place(arr, low, mid)
        merge_sort_in_place(arr, mid + 1, high)
        _merge_indices(arr, low, mid, high)
    return arr


def _merge_indices(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for idx, val in enumerate(temp):
        arr[low + idx] = val


# =====================================================================
# 5. Quick Sort (In-place Partitioning with Median-of-Three Pivot)
# =====================================================================
def quick_sort(arr, low=0, high=None):
    """
    Quick Sort Algorithm:
    Picks a pivot element and partitions the array around the pivot such that
    elements less than or equal to pivot are on the left, and elements greater
    are on the right. Recursively applies the same logic to subarrays.

    Optimization:
    - Median-of-Three pivot selection: compares low, mid, high and picks median
      as pivot. This avoids O(N^2) degradation on already-sorted or reverse-sorted input.

    Characteristics:
    - Time Complexity: Best O(N log N), Average O(N log N), Worst O(N^2)
    - Space Complexity: O(log N) auxiliary recursion call stack
    - Stability: Not stable (swaps non-adjacent elements)
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = _partition_median_of_three(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    return arr


def _partition_median_of_three(arr, low, high):
    """
    Selects the median of arr[low], arr[mid], arr[high] as pivot,
    swaps it to arr[high], and performs Lomuto partitioning.
    """
    mid = (low + high) // 2

    # Sort low, mid, high elements to find median
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    # arr[mid] is now the median; swap it with arr[high] to use as pivot
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# =====================================================================
# Demonstration & Verification
# =====================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRATION OF ALL 5 SORTING ALGORITHMS (OPTIMAL SOLUTIONS)")
    print("=" * 65)

    test_samples = {
        "Random List": [64, 34, 25, 12, 22, 11, 90],
        "Already Sorted": [1, 2, 3, 4, 5, 6, 7],
        "Reverse Sorted": [9, 8, 7, 6, 5, 4, 3, 2, 1],
        "With Duplicates": [4, 2, 5, 2, 3, 4, 1, 1, 5],
        "Single Element": [42],
        "Empty List": [],
    }

    algorithms = [
        ("1. Selection Sort", lambda lst: selection_sort(lst.copy())),
        ("2. Bubble Sort (Optimized)", lambda lst: bubble_sort(lst.copy())),
        ("3. Insertion Sort (Optimized)", lambda lst: insertion_sort(lst.copy())),
        ("4. Merge Sort (Recursive)", lambda lst: merge_sort(lst.copy())),
        ("4b. Merge Sort (In-Place)", lambda lst: merge_sort_in_place(lst.copy())),
        ("5. Quick Sort (Median Pivot)", lambda lst: quick_sort(lst.copy())),
    ]

    for algo_name, algo_fn in algorithms:
        print(f"\n--- {algo_name} ---")
        for test_name, sample in test_samples.items():
            result = algo_fn(sample)
            expected = sorted(sample)
            assert result == expected, f"Failed on {test_name}: {result} != {expected}"
            print(f"  {test_name:<18} Input: {sample!s:<30} -> Sorted: {result}")
        print("  All test cases PASSED!")

    print("\n" + "=" * 65)
    print("All 5 Sorting Algorithms successfully verified with optimal solutions!")
    print("=" * 65)
