'''Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7] '''

def topKFrequent(nums, k):
    from collections import defaultdict

    # Count frequencies
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    print(counts)

    # Bucket sort by frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)
        print(buckets)

    # Gather top k frequent elements
    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

print(topKFrequent([1,2,2,3,3,3], 2))  # Output: [3, 2]
print(topKFrequent([7,7], 1))           # Output: [7]
print(topKFrequent([1], 1))             # Output: [1]
print(topKFrequent([1,2], 2)) 


''' 
defaultdict(<class'int'>, {1: 1, 2: 2, 3: 3})

[[], [1], [], [], [], [], []]
[[], [1], [2], [], [], [], []]
[[], [1], [2], [3], [], [], []]


defaultdict(<class'int'>, {7: 2})

[[], [], [7]]

'''




'''
So, time complexity = O(n).
    Space complexity = O(n).

'''

