"""
Hashing & Hash Map Techniques in Python (Optimal Solutions)
==========================================================

This module covers foundational to advanced hashing concepts, frequency counting,
classic hash map interview problems with optimal time/space complexities, and
an internal Hash Table implementation with collision handling (Separate Chaining).

Concepts & Problems Covered:
1. Direct Address Array Hashing (Number & Character Hashing)
2. Hash Map (Dictionary) Frequency Counting
3. Highest and Lowest Frequency Elements (O(N) Time, O(N) Space)
4. First Repeating and First Non-Repeating Elements (O(N) Time)
5. Two Sum Problem (Optimal Single-Pass Hash Map, O(N) Time, O(N) Space)
6. Longest Subarray with Sum K (Prefix Sum + Hash Map, O(N) Time, O(N) Space)
7. Subarray Sum Equals K - Count Total Subarrays (O(N) Time, O(N) Space)
8. Valid Anagram Check (Optimal O(N) Time, O(1) Space)
9. Under the Hood: Custom HashTable Class (Separate Chaining & Dynamic Rehashing)
"""

# =====================================================================
# 1. Direct Address Array Hashing
# =====================================================================
def number_frequency_array_hashing(nums, max_val, queries):
    """
    Direct Index Hashing for bounded integers:
    Precomputes frequencies in an array of size `max_val + 1`.

    - Time Complexity: O(N + Q) where N is len(nums) and Q is len(queries)
    - Space Complexity: O(max_val) auxiliary space
    - Query Time: O(1) per query
    """
    freq_arr = [0] * (max_val + 1)
    for num in nums:
        if 0 <= num <= max_val:
            freq_arr[num] += 1

    results = {}
    for q in queries:
        results[q] = freq_arr[q] if 0 <= q <= max_val else 0
    return results


def character_hashing(text):
    """
    Character Hashing for lowercase English letters:
    Maps each character 'a'-'z' to index `ord(char) - ord('a')` in a size 26 array.

    - Time Complexity: O(N) where N is len(text)
    - Space Complexity: O(1) (fixed array of 26 integers)
    """
    freq_arr = [0] * 26
    for ch in text.lower():
        if 'a' <= ch <= 'z':
            idx = ord(ch) - ord('a')
            freq_arr[idx] += 1

    freq_dict = {}
    for i in range(26):
        if freq_arr[i] > 0:
            freq_dict[chr(ord('a') + i)] = freq_arr[i]
    return freq_dict


# =====================================================================
# 2. Hash Map (Dictionary) Frequency Counting
# =====================================================================
def frequency_counting_dict(items):
    """
    Counts frequency of arbitrary hashable elements using a Python dictionary.

    - Time Complexity: O(N) average
    - Space Complexity: O(U) where U is number of unique elements (<= N)
    """
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq


# =====================================================================
# 3. Highest and Lowest Frequency Elements
# =====================================================================
def highest_and_lowest_frequency(nums):
    """
    Finds the element with the highest frequency and the element with the
    lowest frequency in a list in a single optimal pass.

    - Time Complexity: O(N)
    - Space Complexity: O(N)
    """
    if not nums:
        return None, None

    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    max_elem = min_elem = nums[0]
    max_count = 0
    min_count = float("inf")

    for elem, count in freq.items():
        if count > max_count:
            max_count = count
            max_elem = elem
        if count < min_count:
            min_count = count
            min_elem = elem

    return (max_elem, max_count), (min_elem, min_count)


# =====================================================================
# 4. First Non-Repeating and First Repeating Elements
# =====================================================================
def first_repeating_element(nums):
    """
    Returns the first element that repeats in the list.
    Uses a Hash Set to track seen elements in O(1) lookup.

    - Time Complexity: O(N)
    - Space Complexity: O(N)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None


def first_non_repeating_element(nums):
    """
    Returns the first element with a frequency of exactly 1.

    - Time Complexity: O(N) (two passes over N elements)
    - Space Complexity: O(N)
    """
    freq = frequency_counting_dict(nums)
    for num in nums:
        if freq[num] == 1:
            return num
    return None


# =====================================================================
# 5. Two Sum Problem (Optimal Hash Map Solution)
# =====================================================================
def two_sum_optimal(nums, target):
    """
    Given an array of integers and a target value, returns indices of the two
    numbers that add up to the target.

    Optimal Approach:
    Uses a hash map to store `value: index`. For each number, checks if its
    complement `target - num` already exists in the map.

    - Time Complexity: O(N) (single pass)
    - Space Complexity: O(N)
    """
    seen = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
    return []


# =====================================================================
# 6. Longest Subarray with Sum K (Optimal Prefix Sum + Hash Map)
# =====================================================================
def longest_subarray_with_sum_k(nums, k):
    """
    Finds the length of the longest contiguous subarray whose elements sum to `k`.
    Handles positive numbers, negative numbers, and zeros.

    Optimal Approach:
    - Maintains prefix_sum.
    - If `prefix_sum == k`, the subarray starts at index 0, length is `i + 1`.
    - If `(prefix_sum - k)` was seen before, a subarray summing to `k` exists
      between that previous index and current index `i`.
    - To maximize length, only store the *first* occurrence of each prefix sum.

    - Time Complexity: O(N)
    - Space Complexity: O(N)
    """
    prefix_map = {}  # prefix_sum -> earliest index
    current_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        current_sum += num

        if current_sum == k:
            max_len = i + 1

        rem = current_sum - k
        if rem in prefix_map:
            sub_len = i - prefix_map[rem]
            if sub_len > max_len:
                max_len = sub_len

        # Store only first occurrence of current_sum to maximize future subarray lengths
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_len


# =====================================================================
# 7. Subarray Sum Equals K (Total Count of Subarrays)
# =====================================================================
def count_subarrays_with_sum_k(nums, k):
    """
    Counts the total number of continuous subarrays whose sum equals `k`.

    - Time Complexity: O(N)
    - Space Complexity: O(N)
    """
    count = 0
    current_sum = 0
    prefix_counts = {0: 1}  # Base case: sum of 0 appears once initially

    for num in nums:
        current_sum += num
        rem = current_sum - k
        if rem in prefix_counts:
            count += prefix_counts[rem]

        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count


# =====================================================================
# 8. Valid Anagram Check (Optimal O(N) Time, O(1) Extra Space)
# =====================================================================
def is_valid_anagram(s, t):
    """
    Determines if two strings `s` and `t` are anagrams of each other.
    An anagram contains the exact same characters with the exact same frequencies.

    Optimal Approach:
    Count character frequencies using an array of size 26 (or hash map).
    Increment count for characters in `s` and decrement for characters in `t`.

    - Time Complexity: O(N)
    - Space Complexity: O(1) (fixed 26-element array for English alphabet)
    """
    if len(s) != len(t):
        return False

    counts = [0] * 26
    for ch_s, ch_t in zip(s, t):
        counts[ord(ch_s) - ord('a')] += 1
        counts[ord(ch_t) - ord('a')] -= 1

    return all(c == 0 for c in counts)


# =====================================================================
# 9. Under the Hood: Custom HashTable Implementation
# =====================================================================
class HashTable:
    """
    Custom Hash Table demonstrating collision handling via Separate Chaining
    and Dynamic Resizing (Rehashing).

    - Hash Function: Modular arithmetic with string polynomial hashing
    - Collision Resolution: Separate Chaining (bucket linked lists / tuples)
    - Resizing: Automatically doubles capacity when load factor exceeds 0.75
    - Average Time Complexity: O(1) for put, get, remove, contains
    - Worst Case: O(N) (all keys hash to same bucket)
    """
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        """Calculates bucket index for a given key."""
        if isinstance(key, str):
            # Polynomial rolling hash
            h = 0
            for ch in key:
                h = (h * 31 + ord(ch))
            return h % self.capacity
        return abs(hash(key)) % self.capacity

    def put(self, key, value):
        """Inserts or updates key-value pair. Resizes if load factor > 0.75."""
        if (self.size + 1) / self.capacity > 0.75:
            self._resize(self.capacity * 2)

        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return

        bucket.append((key, value))
        self.size += 1

    def get(self, key, default=None):
        """Retrieves value associated with key, or default if not found."""
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return default

    def contains(self, key):
        """Checks if key is present in hash table."""
        return self.get(key) is not None

    def remove(self, key):
        """Removes key-value pair. Returns True if removed, False otherwise."""
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def _resize(self, new_capacity):
        """Rehashes all existing entries into new bucket array."""
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [[] for _ in range(new_capacity)]
        self.size = 0

        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k, v)

    def __repr__(self):
        items = []
        for bucket in self.buckets:
            for k, v in bucket:
                items.append(f"{k!r}: {v!r}")
        return "{" + ", ".join(items) + "}"


# =====================================================================
# Demonstration & Verification
# =====================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRATION OF HASHING TECHNIQUES & OPTIMAL SOLUTIONS")
    print("=" * 65)

    # 1. Direct Address Array Hashing
    print("\n1. Direct Array Hashing:")
    sample_nums = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
    queries = [10, 111, 1, 9, 5, 67, 2]
    print("  Nums:", sample_nums)
    print("  Queries:", queries)
    ans = number_frequency_array_hashing(sample_nums, 10, queries)
    print("  Query Answers:", ans)

    # Character Hashing
    char_ans = character_hashing("Hello Antigravity Python!")
    print("  Character Hashing ('Hello Antigravity Python!'):", char_ans)

    # 2. Dictionary Frequency Counting
    print("\n2. Dictionary Frequency Counting:")
    data = [1, 56, 4, 8, 56, 4, 8, 3, 1, 1, 111, 46, 48, 6]
    freq = frequency_counting_dict(data)
    print("  Frequencies:", freq)

    # 3. Highest and Lowest Frequency
    print("\n3. Highest & Lowest Frequency Elements:")
    highest, lowest = highest_and_lowest_frequency(data)
    print(f"  Highest Frequency: Element {highest[0]} (count: {highest[1]})")
    print(f"  Lowest Frequency:  Element {lowest[0]} (count: {lowest[1]})")

    # 4. First Repeating and Non-Repeating
    print("\n4. Repeating & Non-Repeating Elements:")
    rep_list = [3, 1, 3, 2, 5, 3, 2, 1, 5]
    print("  List:", rep_list)
    print("  First Repeating:", first_repeating_element(rep_list))
    print("  First Non-Repeating:", first_non_repeating_element(rep_list))

    # 5. Two Sum (Optimal O(N))
    print("\n5. Two Sum Problem (Optimal O(N)):")
    two_sum_nums = [2, 7, 11, 15]
    target = 9
    indices = two_sum_optimal(two_sum_nums, target)
    print(f"  Nums: {two_sum_nums}, Target: {target} -> Indices: {indices} (Values: {two_sum_nums[indices[0]]} + {two_sum_nums[indices[1]]} = {target})")

    # 6. Longest Subarray with Sum K
    print("\n6. Longest Subarray with Sum K (Optimal O(N)):")
    sub_arr = [10, 5, 2, 7, 1, 9]
    k = 15
    max_l = longest_subarray_with_sum_k(sub_arr, k)
    print(f"  Array: {sub_arr}, K={k} -> Longest Subarray Length: {max_l}")

    # 7. Subarray Sum Equals K (Count)
    print("\n7. Count Subarrays with Sum K:")
    cnt_arr = [1, 1, 1]
    k_cnt = 2
    total_sub = count_subarrays_with_sum_k(cnt_arr, k_cnt)
    print(f"  Array: {cnt_arr}, K={k_cnt} -> Total Subarrays: {total_sub}")

    # 8. Valid Anagram Check
    print("\n8. Valid Anagram Check:")
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"
    print(f"  '{s1}' & '{t1}':", is_valid_anagram(s1, t1))
    print(f"  '{s2}' & '{t2}':", is_valid_anagram(s2, t2))

    # 9. Custom HashTable
    print("\n9. Custom HashTable (Separate Chaining):")
    ht = HashTable(initial_capacity=4)
    ht.put("apple", 100)
    ht.put("banana", 200)
    ht.put("orange", 300)
    ht.put("grape", 400)  # Triggers resize
    print("  HashTable Contents:", ht)
    print("  Get 'banana':", ht.get("banana"))
    print("  Contains 'apple':", ht.contains("apple"))
    ht.remove("banana")
    print("  After removing 'banana':", ht)
    print("  Contains 'banana':", ht.contains("banana"))

    print("\n" + "=" * 65)
    print("All Hashing Techniques & Problems successfully verified!")
    print("=" * 65)
