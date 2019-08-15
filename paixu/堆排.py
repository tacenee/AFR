def max_heap(arr, parent, arr_len):
    # left & right node index
    left = 2 * parent + 1
    right = 2 * parent + 2
    max_not = parent
    if left < arr_len and arr[left] > arr[parent]:
        parent = left
    if right < arr_len and arr[right] > arr[parent]:
        parent = right

    if max_not != parent:
        arr[parent], arr[max_not] = arr[max_not], arr[parent]
        max_heap(arr, parent, arr_len)


def dui_sort(arr):
    n = len(arr)
    # creat max heap
    for j in range(n // 2, -1, -1):
        max_heap(arr, j, n)
    for i in range(n, 0, -1):
        arr[0], arr[i - 1] = arr[i - 1], arr[0]
        max_heap(arr, 0, i - 1)

# def duipai(nums):
#     length = len(nums)
#     for i in range(length // 2, -1, -1):
#         maxHeap(nums, length, i)
#
#     for i in range(length, 0, -1):
#         nums[0], nums[i - 1] = nums[i - 1], nums[0]
#         maxHeap(nums, i - 1, 0)
#
#
# def maxHeap(nums, heapSize, index):
#     left = index * 2 + 1
#     right = index * 2 + 2
#     # cur_max = nums[index]
#     parent = index
#     if left < heapSize and nums[left] > nums[parent]:
#         parent = left
#     if right < heapSize and nums[right] > nums[parent]:
#         parent = right
#     if parent != index:
#         nums[parent], nums[index] = nums[index], nums[parent]
#         maxHeap(nums, heapSize, parent)


arr = [12, 11, 13, 5, 6, 7]
# dui_sort(arr)
duipai(arr)
n = len(arr)
print("排序后")
for i in range(n):
    print("%d" % arr[i])
