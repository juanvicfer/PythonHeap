
import heapq


def kth_min_element(k, input_array):
    heapq.heapify(input_array)

    for elem in range(k-1):
        heapq.heappop(input_array)

    return heapq.heappop(input_array)


cases = int(input())

for i in range(cases):
    size = int(input())
    array = [int(s) for s in input().split()]
    k = int(input())

    print(kth_min_element(k, array))


