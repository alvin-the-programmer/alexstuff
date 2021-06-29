

# Given a list of numbers, return the k largest numbers


# k = 3
# numbers = [10, 4, 6, 12, 15, 2, 2, 9]

# O(n * k) # O(n^2)
import heapq


def top_k(numbers, k):
    current_numbers = numbers[:]
    result = []

    for i in range(0, k):
        next_max = max(current_numbers)
        result.append(next_max)
        current_numbers = current_numbers[:]
        current_numbers.remove(next_max)

    return result


# O(nlogn + k) # O(nlogn)
def top_k(numbers, k):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[:k]


# O(nlogk + klogk + k)


k = 3
numbers = [10, 4, 6, 12, 15, 2, 2, 9]
#                                       ^

# maintain a heap of size k = 3


# HEAP:
# (10) 12 15

# [10,12,15]


def top_k(numbers, k):
    heap = []
    for num in numbers:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    new_numbers = []
    print(heap)
    while heap:
        new_numbers.append(heapq.heappop(heap))
    return new_numbers[::-1]


k = 3
numbers = [10, 4, 6, 12, 15, 2, 2, 9]
print(top_k(numbers, k))
